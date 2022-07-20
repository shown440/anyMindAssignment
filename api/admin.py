from django.contrib import admin
from .models import AttandenceModel


class AttandenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_id', 'in_time', 'out_time']  
    
    class Meta:
        model = AttandenceModel



# Register your models here.
admin.site.register(AttandenceModel, AttandenceAdmin) 
