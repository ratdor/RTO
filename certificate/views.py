from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate 
from django.contrib import messages
from .forms import OwnerForm
from .models import Owner
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
import qrcode
from io import BytesIO
import base64
from django.urls import reverse
from django.http import HttpRequest
from django.db.models import Q,F
from datetime import datetime

def login_view(request):
    if request.method == "POST":
        name = request.POST.get('username')
        pswd = request.POST.get('password')
        user = authenticate(request,username=name,password=pswd)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfully")
            return redirect('home/')
        else:
            messages.error(request,"Login UnSuccessfully")
            return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='/login/')
def home_view(request):
    if request.method == 'POST':
        owner_form = OwnerForm(request.POST, request.FILES)
        if owner_form.is_valid():
            owner = owner_form.save(commit=False)
            owner.save(using='mysql')  # Save to MySQL
            return redirect('search')
    else:
        owner_form = OwnerForm()
    
    context = {
        'owner_form': owner_form,
    }
    return render(request, 'home.html', context)

@login_required(login_url='/login/')
def success_view(request):
    return render(request,'success.html')

def logout_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Logout Successful")
        return redirect('login')
    else:
        return HttpResponseNotAllowed(['GET'])

    
def search_view(request):
    queryset_by_date_vehicle = []
    formatted_date = datetime.now().date()  # Get current date

    if request.method == "POST":
        vehic_no = request.POST.get('vecregno')

        if vehic_no:
            # Filtering by vehicle number (case insensitive)
            queryset_by_date_vehicle = Owner.objects.filter(vehicle_no__icontains=vehic_no)

        from_date_str = request.POST.get('from_date', None)
        to_date_str = request.POST.get('to_date', None)
        
        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, "%Y-%m-%d").date()
            to_date = datetime.strptime(to_date_str, "%Y-%m-%d").date()
            # Filtering by date range
            queryset_by_date_vehicle = Owner.objects.filter(today_date__range=[from_date, to_date])

    else:
        # Fetching all unique data from SQLite and MySQL
        sqlite_data = Owner.objects.using('default').all()
        mysql_data = Owner.objects.using('mysql').all()

        combined_data = {}

        # Adding SQLite data to combined_data dictionary
        for owner in sqlite_data:
            combined_data[owner.id] = owner

        # Adding MySQL data to combined_data dictionary, avoiding duplicates
        for owner in mysql_data:
            combined_data.setdefault(owner.id, owner)

        # Converting combined_data dictionary values back to a list
        queryset_by_date_vehicle = list(combined_data.values())

    context = {
        'queryset_by_date_vehicle': queryset_by_date_vehicle,
        'formatted_date': formatted_date.strftime("%m/%d/%Y"),  # Formatting date for display
    }
    return render(request, 'search_original.html', context)

def certificate_view(request, id):
    certificate_details = None
    
    # Try fetching from SQLite first
    try:
        certificate_details = Owner.objects.using('default').get(id=id)
    except Owner.DoesNotExist:
        pass
    
    # If not found in SQLite, try fetching from MySQL
    if not certificate_details:
        try:
            certificate_details = Owner.objects.using('mysql').get(id=id)
        except Owner.DoesNotExist:
            pass
    
    if not certificate_details:
        return render(request, "certificate_view.html", {
            'certificate': None,
            'qr_image_url': None,
            'error_message': 'Certificate not found in both databases.',
        })

    # Generate QR code
    user_data_url = request.build_absolute_uri(reverse('user_data', args=[certificate_details.id]))
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=5,
    )
    qr.add_data(user_data_url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    qr_image.save(buffer, format="PNG")
    qr_image_data = base64.b64encode(buffer.getvalue()).decode()
    qr_image_url = f"data:image/png;base64,{qr_image_data}"

    context = {
        'certificate': certificate_details,
        'qr_image_url': qr_image_url,
    }

    return render(request, "certificate_view.html", context)


def user_data_view(request, user_id):
    user_data = None

    # Try fetching from SQLite first
    try:
        user_data = Owner.objects.using('default').get(id=user_id)
    except Owner.DoesNotExist:
        # If not found in SQLite, try fetching from MySQL
        try:
            user_data = Owner.objects.using('mysql').get(id=user_id)
        except Owner.DoesNotExist:
            user_data = None
    
    context = {
        'user_data': user_data,
    }
    return render(request, 'user_data.html', context)



