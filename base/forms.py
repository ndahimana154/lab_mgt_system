# forms.py
from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    
class EquipmentTypeForm(forms.ModelForm):
    class Meta:
        model = LabEquipmentType
        fields = ['type_name']
        
class EquipmentTypeForm(forms.ModelForm):
    class Meta:
        model = LabEquipmentType
        fields = ['type_name']
        

class LabEquipmentForm(forms.ModelForm):
    class Meta:
        model = LabEquipment
        exclude = ['availability_status']  # Exclude the availability_status field

    def clean_serial_number(self):
        serial_number = self.cleaned_data['serial_number']
        if LabEquipment.objects.filter(serial_number=serial_number).exists():
            raise forms.ValidationError("This serial number already exists. Please enter a unique serial number.")
        return serial_number
    

class EquipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = LabEquipment
        fields = ['name', 'description', 'equipment_type', 'availability_status', 'purchase_date']