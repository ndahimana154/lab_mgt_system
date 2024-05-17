from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group,Permission
from django.db import models


class SystemUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=15)
    password=models.CharField(max_length=300)
    user_type = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    
class LabEquipmentType(models.Model):
    type_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.type_name

class LabEquipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    serial_numbers = models.CharField(max_length=200, unique=True)  # Ensure uniqueness of serial numbers
    equipment_type = models.ForeignKey(LabEquipmentType, on_delete=models.CASCADE)
    availability_status = models.BooleanField(default=True)
    purchase_date = models.DateField()

    def __str__(self):
        return self.name
    

    

