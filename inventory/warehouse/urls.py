from django.urls import path

from . import views

app_name = 'warehouse'
urlpatterns=[
	path('list_warehouses/', views.warehouse_home, name="WarehouseHome"),
	path('create_warehouse/', views.create_warehouse, name = "CreateWarehouse"),
	path('publish_warehouse/<int:warehouse_id>/', views.publish_warehouse, name = "PublishWarehouse"),
	path('activate_warehouse/<int:warehouse_id>/', views.activate_warehouse, name = "ActivateWarehouse"),
]

