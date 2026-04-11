from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from .models import Property
from .forms import PropertyForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PropertySerializer

# ─── WEB VIEWS ──────────────────────────────────────────────

@login_required
def property_list(request):
    search = request.GET.get('search', '')
    property_type = request.GET.get('type', '')
    status_filter = request.GET.get('status', '')
    
    properties = Property.objects.all()
    
    if search:
        properties = properties.filter(address__icontains=search) | properties.filter(owner_name__icontains=search)
    if property_type:
        properties = properties.filter(property_type=property_type)
    if status_filter:
        properties = properties.filter(status=status_filter)

    # Stats for dashboard
    total = Property.objects.count()
    total_value = Property.objects.aggregate(Sum('value'))['value__sum'] or 0
    by_type = Property.objects.values('property_type').annotate(count=Count('id'))
    by_status = Property.objects.values('status').annotate(count=Count('id'))

    return render(request, 'properties/property_list.html', {
        'properties': properties,
        'search': search,
        'total': total,
        'total_value': total_value,
        'by_type': by_type,
        'by_status': by_status,
        'property_type': property_type,
        'status_filter': status_filter,
    })

@login_required
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})

@login_required
def property_add(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.registered_by = request.user
            property.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/property_add.html', {'form': form})

@login_required
def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'properties/property_edit.html', {'form': form, 'property': property})

@login_required
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'properties/property_delete.html', {'property': property})

# ─── API VIEWS ──────────────────────────────────────────────

@api_view(['GET', 'POST'])
def api_property_list(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'GET':
        serializer = PropertySerializer(property)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)