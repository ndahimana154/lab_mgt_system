from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # Login
    path("login/",views.login_view, name="login"),
    # Home for users
    path("",views.home_view,name="home"),
    # View equipments types list
    path("equipments/types/",views.equipment_types_list,name="equipment_types_list"),
    # Delete Equipments types
     path('equipment_types/<int:equipment_type_id>/delete/', views.delete_equipment_type, name='delete_equipment_type'),
    # Delete Equipments types
     path('equipment_types/<int:equipment_type_id>/update/', views.update_equipment_type, name='update_equipment_type'),
    # New equipments types
    path("equipments/types/new/",views.equipment_types_form,name="equipment_types_form"),
    
    # Equipments List
    path("equipments/",views.equipments_list,name="equipments_list"),
    # Delete equipments
    path('equipments/<int:equipment_id>/delete/', views.delete_equipment, name='delete_equipment'),
    # Update the equipments
    path('update/<int:equipment_id>/', views.update_equipment_view, name='update_equipment'),
    # New equipments 
    path("equipments/new",views.create_equipment,name="equipments_form"),
    
    # Logout
    path("logout/",views.logout_view,name="logout")
]
