from django.contrib import admin
from .models import *

# Register your models here.
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_at']

admin.site.register(Country, CountryModelAdmin)

class StateModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'name', 'created_at']

admin.site.register(State, StateModelAdmin)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id','country','state','name','created_at']

admin.site.register(District, DistrictAdmin)

class PrefjobLocationAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_at']

admin.site.register(prejobloc, PrefjobLocationAdmin)

class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','mobile','is_active','created_at']

admin.site.register(employeeDetails,EmployeeDetailsAdmin)
