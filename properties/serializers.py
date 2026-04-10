from rest_framework import serializers
from .models import Property

# This converts Property objects to JSON and back
# JSON is the language APIs use to send data
# Example output:
# {
#     "id": 1,
#     "address": "123 Harare Street",
#     "owner_name": "John Moyo",
#     "size": "250.00",
#     "property_type": "house",
#     "date_registered": "2024-01-01"
# }
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'  # Include all fields