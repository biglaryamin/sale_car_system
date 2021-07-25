from django.contrib import admin
from .models import *



class CarAdmin(admin.ModelAdmin):
    list_display=('car_name','car_id','color')
    search_fields=('car_id','car_name')
    ordering=['car_name']

admin.site.register(Car,CarAdmin)





admin.site.register(Person)
