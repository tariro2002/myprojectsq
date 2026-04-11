from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = ['address', 'owner_name', 'city', 'property_type', 'status', 'value', 'date_registered']
    
    # Filters on the right side
    list_filter = ['property_type', 'status', 'city', 'province']
    
    # Search fields
    search_fields = ['address', 'owner_name', 'owner_email', 'city']
    
    # Make status editable directly from list
    list_editable = ['status']
    
    # Order by newest first
    ordering = ['-date_registered']
    
    # Group fields into sections
    fieldsets = (
        ('Owner Information', {
            'fields': ('owner_name', 'owner_email', 'owner_phone')
        }),
        ('Property Details', {
            'fields': ('address', 'city', 'province', 'property_type', 'status', 'size', 'value')
        }),
        ('GPS Location', {
            'fields': ('gps_latitude', 'gps_longitude'),
            'classes': ('collapse',)
        }),
        ('Additional', {
            'fields': ('image', 'notes', 'registered_by')
        }),
    )