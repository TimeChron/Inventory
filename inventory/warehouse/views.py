from django.shortcuts import render, redirect
from .models import Store
from .forms import WarehouseCreateForm
from django.urls import reverse
from django.views import View
from datetime import datetime

def warehouse_home(request):
    ## This view is for warehouse home
    ## Load all the warehouse objects and show them in a list at warehouse_home

    warehouses = Store.objects.all()
    return render(request, 'warehouse/warehouse_home.html', {'warehouses': warehouses})

def create_warehouse(request):
    if request.method == "POST":
        form = WarehouseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('warehouse:WarehouseHome')
            return redirect(url)
    else:
        form = WarehouseCreateForm()
    return render(request, 'warehouse/create_warehouse.html', {'form': form})

def publish_warehouse(request, warehouse_id):
    ## Load the warehouse_object
    warehouse_obj = Store.objects.filter(id = warehouse_id).first()
    warehouse_obj.publish = True
    warehouse_obj.published_at = datetime.now()
    warehouse_obj.published_by = request.user.id
    warehouse_obj.save()
    url = reverse('warehouse:WarehouseHome')
    return redirect(url)

def activate_warehouse(request, warehouse_id):
    ## Load the warehouse_object
    warehouse_obj = Store.objects.filter(id = warehouse_id).first()
    warehouse_obj.active = not warehouse_obj.active
    warehouse_obj.save()
    url = reverse('warehouse:WarehouseHome')
    return redirect(url)


