from django.db import models 

from django.conf import settings



# Create your models here. 

def upload_status_image(instance, filename): #instance, 
    return "application/{filename}".format(filename=filename)  
#     # static-server/media-root/


####################################################################
### Model for Attandence Table
####################################################################
class AttandenceModel(models.Model):

    employee_id     = models.IntegerField(blank=True, null=True)
    to_date         = models.DateField(blank=True, null=True)
    in_time         = models.DateTimeField(blank=True, null=True)
    out_time        = models.DateTimeField(blank=True, null=True)
    total_hours     = models.IntegerField(blank=True, null=True)

    created_by      = models.IntegerField(blank=True, null=True)
    created_at      = models.DateTimeField(auto_now=True, blank=True, null=True) 
    updated_by      = models.IntegerField(blank=True, null=True)
    updated_at      = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return str(self.employee_id)

    class Meta:
        managed = True
        db_table = "attandence_details"
        
        verbose_name = 'Attandence Detail'
        verbose_name_plural = 'Attandence Details'  


