from django.urls import path

from .views import WarehouseView 

app_name = 'warehouse'
urlpatterns=[
	path('', WarehouseView.warehouse_home, name="WarehouseHome")
]