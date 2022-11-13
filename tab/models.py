from django.db import models
from django.forms import BooleanField

# Create your models here.

class Machine(models.Model):
  name = models.CharField(max_length=100)
  gps_loc = models.CharField(max_length=200)
  description = models.TextField()
  barcode = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

class Farmer(models.Model):
  name = models.CharField(max_length=100)
  product_type = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

class ServiceProvider(models.Model):
  syn_available_machine = models.BooleanField(default=False)
  confirm_message = models.BooleanField(default=False)
  payment = models.CharField(max_length=100,unique=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


class ExcelFile(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    excel_file = models.FileField(upload_to='excel', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)
