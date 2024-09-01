from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer

class InventoryDetailView(generics.RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = 'station_id'

from django.http import JsonResponse

def get_inventory_ids(request):
    inventory_ids = Inventory.objects.values_list('station_id', flat=True)
    return JsonResponse(list(inventory_ids), safe=False)
