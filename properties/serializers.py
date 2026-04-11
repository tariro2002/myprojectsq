from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    # This shows the username instead of just the ID
    registered_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Property
        fields = '__all__'  # Include all fields including new ones

    def validate_size(self, value):
        # Make sure size is positive
        if value <= 0:
            raise serializers.ValidationError("Size must be greater than 0")
        return value

    def validate_value(self, value):
        # Make sure value is positive if provided
        if value and value <= 0:
            raise serializers.ValidationError("Value must be greater than 0")
        return value