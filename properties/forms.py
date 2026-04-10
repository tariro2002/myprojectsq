from django import forms
from .models import Property

# This creates a form based on our Property model
# Django will automatically create input fields
# for each field in the model
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['address', 'owner_name', 'size', 'property_type']