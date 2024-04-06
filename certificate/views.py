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
        owner_form = OwnerForm(request.POST,request.FILES)
        if owner_form.is_valid():
            owner = owner_form.save()
            return redirect('search')
    else:
        owner_form = OwnerForm()
    
    context ={
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
    
# def search_view(request):
#     # Searching by vehicle number
#     vehic_no = request.POST.get('vecregno')
#     queryset_by_vehicle = Owner.objects.all()
#     if vehic_no:
#         queryset_by_vehicle = queryset_by_vehicle.filter(vehicle_no__icontains=vehic_no)

#     context = {
#         'trans_no': queryset_by_vehicle,
#     }
#     return render(request, 'search_original.html', context)

# def search_view(request):
#     queryset_by_date = []
#     if request.method == "POST":
#         # Get dates from the POST request
#         from_date_str = request.POST.get('from_date', None)
#         to_date_str = request.POST.get('to_date', None)
        
#         # Convert string dates to datetime objects
#         if from_date_str and to_date_str:
#             from_date_str = datetime.strptime(from_date_str, "%Y-%m-%d").date()
#             to_date_str = datetime.strptime(to_date_str, "%Y-%m-%d").date()
            
#             # Filter your queryset based on the date range
#             queryset_by_date = Owner.objects.filter(today_date__range=[from_date_str , to_date_str])
#     else:
#         # Handle non-POST requests if necessary, such as displaying an empty form
#         # queryset_by_date can be an empty queryset or a queryset with all objects based on your needs
#         queryset_by_date = Owner.objects.all()

#     # Pass the filtered queryset to the template
#     context = {'queryset_by_date': queryset_by_date}
#     return render(request, 'search_original.html', context)
    
def search_view(request):
    queryset_by_date_vehicle = []
    formatted_date = datetime.now().date()  # Ensuring formatted_date has a default value

    if request.method == "POST":
        vehic_no = request.POST.get('vecregno')
        if vehic_no:
            queryset_by_date_vehicle = Owner.objects.filter(vehicle_no__icontains=vehic_no,id=1)

        from_date_str = request.POST.get('from_date', None)
        to_date_str = request.POST.get('to_date', None)
        
        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, "%Y-%m-%d").date()
            to_date = datetime.strptime(to_date_str, "%Y-%m-%d").date()
            # It seems you wanted to filter objects up to the current date but included formatted_date incorrectly.
            queryset_by_date_vehicle = Owner.objects.filter(today_date__range=[from_date, to_date])

    else:
        queryset_by_date_vehicle = Owner.objects.all()

    context = {
        'queryset_by_date_vehicle': queryset_by_date_vehicle,
        'formatted_date': formatted_date.strftime("%m/%d/%Y"),  # Properly formatting the date here for display
    }
    return render(request, 'search_original.html', context)


def certificate_view(request, id):
    try:
        certificate_details = Owner.objects.get(id=id)
    
        user_data_url = request.build_absolute_uri(reverse('user_data', args=[certificate_details.id]))
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=5,
        )
        qr.add_data(user_data_url)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        qr_image_data = base64.b64encode(buffer.getvalue()).decode()
        qr_image_url = f"data:image/png;base64,{qr_image_data}"
    except Owner.DoesNotExist:
        certificate_details = None
        qr_image_url = None
    
    context = {
        'certificate': certificate_details,
        'qr_image_url': qr_image_url,
    }
    
    return render(request, "certificate_view.html", context)


def user_data_view(request,user_id):
   
    try:
         user_data = Owner.objects.get(id= user_id)
    except Owner.DoesNotExist:
        user_data = None
    
    context = {
        'user_data': user_data,
    }
    return render(request,'user_data.html',context)



