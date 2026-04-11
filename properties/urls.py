
from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('<int:pk>/', views.property_detail, name='property_detail'),
    path('add/', views.property_add, name='property_add'),
    path('<int:pk>/edit/', views.property_edit, name='property_edit'),
    path('<int:pk>/delete/', views.property_delete, name='property_delete'),
    path('api/', views.api_property_list, name='api_property_list'),
    path('api/<int:pk>/', views.api_property_detail, name='api_property_detail'),
]