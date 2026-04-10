from django.db import models

# This is our Property model
# Think of it as a table in the database
# Each property will have these fields

class Property(models.Model):

    # The address of the property e.g "123 Harare Street"
    address = models.CharField(max_length=255)

    # The name of the owner e.g "John Moyo"
    owner_name = models.CharField(max_length=255)

    # The size of the property in square meters
    size = models.DecimalField(max_digits=10, decimal_places=2)

    # The type of property e.g house, land, commercial
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ]
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)

    # The date this record was added — fills in automatically
    date_registered = models.DateTimeField(auto_now_add=True)

    # This controls how the property shows up in the admin panel
    def __str__(self):
        return f"{self.address} - {self.owner_name}"