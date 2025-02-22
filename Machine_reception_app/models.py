from django.db import models

# Create your models here.

class Mahcine_reception(models.Model):
    MN = models.AutoField(primary_key=True)
    technician_name=models.CharField(max_length=50, blank=True)
    shelf=models.CharField(max_length=50,blank=True)
    MRC=models.CharField(max_length=50)
    

    def __str__(self):
         return self.MRC+' '+self.shelf