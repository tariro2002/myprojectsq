from django.shortcuts import render, get_object_or_404, redirect
from .models import Property
from .forms import PropertyForm

# REST API imports
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PropertySerializer

# ─── NORMAL WEB VIEWS ───────────────────────────────────────

# Shows list of all properties with optional search
def property_list(request):
    search = request.GET.get('search', '')
    if search:
        properties = Property.objects.filter(address__icontains=search) | Property.objects.filter(owner_name__icontains=search)
    else:
        properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties, 'search': search})

# Shows details of one property
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})

# Handles adding a new property
def property_add(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/property_add.html', {'form': form})

# Handles editing an existing property
def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties/property_edit.html', {'form': form, 'property': property})

# Handles deleting a property
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'properties/property_delete.html', {'property': property})


# ─── API VIEWS ──────────────────────────────────────────────
# These are used by Postman and other apps
# They return JSON data instead of HTML pages

# GET all properties or POST a new one
@api_view(['GET', 'POST'])
def api_property_list(request):
    if request.method == 'GET':
        # Return all properties as JSON
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new property from JSON data
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT or DELETE a single property
@api_view(['GET', 'PUT', 'DELETE'])
def api_property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == 'GET':
        # Return one property as JSON
        serializer = PropertySerializer(property)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update a property with new JSON data
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete a property
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)