from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):

    # Property Types
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
        ('apartment', 'Apartment'),
        ('farm', 'Farm'),
    ]

    # Property Status
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('sold', 'Sold'),
        ('disputed', 'Disputed'),
        ('pending', 'Pending'),
    ]

    # Basic Info
    address = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    owner_email = models.EmailField(blank=True)
    owner_phone = models.CharField(max_length=20, blank=True)

    # Property Details
    size = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    # Location
    city = models.CharField(max_length=100, default='Harare')
    province = models.CharField(max_length=100, default='Harare')
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Image
    image = models.ImageField(upload_to='properties/', null=True, blank=True)

    # Audit Trail
    date_registered = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.address} - {self.owner_name}"

    class Meta:
        ordering = ['-date_registered']
        verbose_name_plural = 'Properties'