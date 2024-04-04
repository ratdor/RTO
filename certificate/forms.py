from django import forms
from .models import Owner

class OwnerForm(forms.ModelForm):
    
    MAKE_CHOICES = [
        ("", "Select"),
        ("AJAX ENGINEERING PVT LTD", "AJAX ENGINEERING PVT LTD"),
        ("AMW", "AMW"),
        ("ASHOK LEYLAND LTD", "ASHOK LEYLAND LTD"),
        ("Atul auto LTD", "Atul auto LTD"),
        ("BAJAJ", "BAJAJ"),
        ("BHARATH BENZ", "BHARATH BENZ"),
        ("BMW INDIA PVT LTD", "BMW INDIA PVT LTD"),
        ("CNH IND PVT LTD", "CNH IND PVT LTD"),
        ("DAIMLER INDIA", "DAIMLER INDIA"),
        ("E ROYCE MOTORS INDIA PVT LTD", "E ROYCE MOTORS INDIA PVT LTD"),
        ("ECO DYNAAMIC EQUIPMENTS", "ECO DYNAAMIC EQUIPMENTS"),
        ("EICHER MOTORS LTD", "EICHER MOTORS LTD"),
        ("ESCORTS LTD", "ESCORTS LTD"),
        ("FORCE MOTORS LIMITED, A FIRODIA ENTERPRISE", "FORCE MOTORS LIMITED, A FIRODIA ENTERPRISE"),
        ("FORCE MOTORS LIMTED", "FORCE MOTORS LIMTED"),
        ("FORD", "FORD"),
        ("FORD INDIA PLTD", "FORD INDIA PLTD"),
        ("FORD INDIA PVT LTD", "FORD INDIA PVT LTD"),
        ("GENERAL MOTORS", "GENERAL MOTORS"),
        ("GUJARATH TRACTOR CORP LTD", "GUJARATH TRACTOR CORP LTD"),
        ("HINDUSTAN MOTORS", "HINDUSTAN MOTORS"),
        ("HMT 212 TRACTOR", "HMT 212 TRACTOR"),
        ("HONDA", "HONDA"),
        ("HYUNDAI", "HYUNDAI"),
        ("ISUZU MOTORS INDIA PVT LTD", "ISUZU MOTORS INDIA PVT LTD"),
        ("JCB INDIA LIMITED", "JCB INDIA LIMITED"),
        ("JOHN DEERE EQUIPMENTS PVT LTD", "JOHN DEERE EQUIPMENTS PVT LTD"),
        ("KIA", "KIA"),
        ("KINETIC GREEN ENERGY & POWERS", "KINETIC GREEN ENERGY & POWERS"),
        ("KIRLOSKAR PNEUMATIC CO LTD", "KIRLOSKAR PNEUMATIC CO LTD"),
        ("MAHINDRA & MAHINDRA LIMITED", "MAHINDRA & MAHINDRA LIMITED"),
        ("MAHINDRA NAVISTAR", "MAHINDRA NAVISTAR"),
        ("MAHINDRA NAVISTAR AUTO LTD", "MAHINDRA NAVISTAR AUTO LTD"),
        ("MAHINDRA NAVISTAR AUTOMOTIVES", "MAHINDRA NAVISTAR AUTOMOTIVES"),
        ("MAN", "MAN"),
        ("MARUTI SUZUKI", "MARUTI SUZUKI"),
        ("MASKTRO MOTORS", "MASKTRO MOTORS"),
        ("MERCEDES- BENZ INDIA", "MERCEDES- BENZ INDIA"),
        ("NISSAN", "NISSAN"),
        ("OMEGA SEIKI EV", "OMEGA SEIKI EV"),
        ("OMEGA SEIKI PVT LTD", "OMEGA SEIKI PVT LTD"),
        ("PIAGGIO", "PIAGGIO"),
        ("REEP INDUUSTRIES PVT LTD", "REEP INDUUSTRIES PVT LTD"),
        ("RENAULT", "RENAULT"),
        ("SAARTHI SHAVAK", "SAARTHI SHAVAK"),
        ("SCOOTERS INDIA LTD", "SCOOTERS INDIA LTD"),
        ("SKODA AUTO INDIA PVT LTD", "SKODA AUTO INDIA PVT LTD"),
        ("SML ISUZU LTD", "SML ISUZU LTD"),
        ("SONALIKA INTERNATIONAL LTD", "SONALIKA INTERNATIONAL LTD"),
        ("SWARAJ MAZDA", "SWARAJ MAZDA"),
        ("TATA MOTORS LTD", "TATA MOTORS LTD"),
        ("TELCO", "TELCO"),
        ("THIRUMALA AGROINDUSTRY", "THIRUMALA AGROINDUSTRY"),
        ("TOYOTA KIRLOSKAR", "TOYOTA KIRLOSKAR"),
        ("TRACTOR & FARM EQUIPMENT STANES MOTORS", "TRACTOR & FARM EQUIPMENT STANES MOTORS"),
        ("TVS", "TVS"),
        ("VE COMMERCIAL", "VE COMMERCIAL"),
        ("VIKRAM AUTO", "VIKRAM AUTO"),
        ("VOLVO", "VOLVO"),
        ("VSL INDUSTRIES LTD", "VSL INDUSTRIES LTD"),
    ]

    make = forms.ChoiceField(choices=MAKE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'onChange': 'getModel();', 'id': 'Make', 'name': 'Make'}))

    class Meta:
        model = Owner
        fields = ['name', 'address', 'phone', 'rto','today_date',
                  'make', 'new_vehicle_registration', 'vehicle_no', 'year_of_registration', 
                  'chassis_no', 'engine_no','vehicle_model','red20mm','red50mm','yellow50mm',
                  'white80mm','class3','white20mm','white50mm','red80mm','yellow80mm','class4','certificate_no',
                  'front_image', 'back_image', 'left_image', 'right_image', 'rc_image']
        
        widgets={
            'today_date':forms.DateInput(attrs={'type':'hidden'}),
            # 'name':forms.TextInput(attrs={'type':'text','class':'form-control','onChange':'getProduct()','id':'Model','name':'Model'})
        }