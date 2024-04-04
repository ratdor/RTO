from django.contrib import admin
from .models import Owner

class OwnerAdmin(admin.ModelAdmin):
    list_display = [
        'name','address','phone','rto','today_date'
    ]

admin.site.register(Owner,OwnerAdmin)
