from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'address', 'owner_name', 'owner_email', 'owner_phone',
            'size', 'property_type', 'status', 'value',
            'city', 'province', 'gps_latitude', 'gps_longitude',
            'image', 'notes'
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }