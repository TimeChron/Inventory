from django.shortcuts import render
from .models import Store
from django.views import View

class WarehouseView(View):
	def warehouse_home(self, request = None):
		## This view is for warehouse home
		## Load all the warehouse objects and show then in list at warehouse_home

		warehouses = Store.objects.all()
		return render(request, 'warehouse/warehouse_home.html', {'warehouses': warehouses})

