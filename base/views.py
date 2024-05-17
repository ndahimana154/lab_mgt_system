# views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# Create your views here.
def login(request,user):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('home')  # Replace 'home' with your home page URL name
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form data.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

# @login_required(login_url='/login/')
def home_view(request):
    total_equipments_count = LabEquipment.objects.count()
    return render(request, 'home.html',{'total_equipments_count': total_equipments_count})


# Equipments types List:
def equipment_types_list(request):
    equipment_types = LabEquipmentType.objects.all()
    return render(request, 'equipment_types_list.html', {'equipment_types': equipment_types})


# Delete the Equipments type
def delete_equipment_type(request, equipment_type_id):
    equipment_type = get_object_or_404(LabEquipmentType, pk=equipment_type_id)
    type_name = equipment_type.type_name  # Store type_name before deletion
    equipment_type.delete()
    messages.success(request, f'"{type_name}" deleted successfully.')  # Use stored type_name in success message
    return redirect('equipment_types_list')

# Update equipment type form
def update_equipment_type(request, equipment_type_id):
    equipment_type = get_object_or_404(LabEquipmentType, pk=equipment_type_id)
    
    if request.method == 'POST':
        form = EquipmentTypeForm(request.POST, instance=equipment_type)
        if form.is_valid():
            form.save()
            return redirect('equipment_types_list')
    else:
        form = EquipmentTypeForm(instance=equipment_type)
    
    return render(request, 'update_equipment_type.html', {'form': form})

# New equpment type form
def equipment_types_form(request):
    result_message = None

    if request.method == 'POST':
        form = EquipmentTypeForm(request.POST)
        if form.is_valid():
            type_name = form.cleaned_data['type_name']
            if LabEquipmentType.objects.filter(type_name=type_name).exists():
                result_message = "Error: This equipment type already exists."
            else:
                form.save()
                result_message = "Equipment type added successfully!"
                form = EquipmentTypeForm()  # Reset the form for a new entry
    else:
        form = EquipmentTypeForm()
    
    return render(request, 'equipment_types_form.html', {'form': form, 'result_message': result_message})


# Equipments lsit
def equipments_list(request):
    equipments = LabEquipment.objects.all()
    return render(request, 'equipments_list.html', {'equipments': equipments})
# Delete the equipment
def delete_equipment(request, equipment_id):
    equipment = get_object_or_404(LabEquipment, id=equipment_id)
    if request.method == 'GET':
        equipment.delete()
        return redirect('equipments_list')  # Redirect to the equipment list page
    return redirect('equipments_list')


def update_equipment_view(request, equipment_id):
    equipment = get_object_or_404(LabEquipment, id=equipment_id)
    
    if request.method == 'POST':
        form = EquipmentUpdateForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, "Update succeeded")
            return redirect('update_equipment', equipment_id=equipment_id)
            # Redirect to equipment list page after successful update
    else:
        form = EquipmentUpdateForm(instance=equipment)
    return render(request, 'update_equipment.html', {'form': form})
# New equipment
def create_equipment(request):
    if request.method == 'POST':
        form = LabEquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = LabEquipmentForm()
            messages.success(request, 'Lab equipment created successfully!')
        else:
            messages.error(request, 'Failed to create lab equipment. Please correct the errors.')
    else:
        form = LabEquipmentForm()
    return render(request, 'new_equipment.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')    