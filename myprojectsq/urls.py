from django.contrib import admin
from django.urls import path, include

# This is the main URL file for the whole project
# It connects the admin panel and the properties app URLs
urlpatterns = [
    # Admin panel at /admin/
    path('admin/', admin.site.urls),

    # All properties pages start with /properties/
    path('properties/', include('properties.urls')),
]