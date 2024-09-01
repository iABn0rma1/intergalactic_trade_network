from django.urls import path
from .views import InventoryDetailView, get_inventory_ids

urlpatterns = [
    # path('inventory/', get_inventory_ids, name='get_inventory_ids'),
    path('inventory/<str:station_id>/', InventoryDetailView.as_view(), name='inventory-detail'),
]
