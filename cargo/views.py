from rest_framework import generics
from .models import Cargo
from .serializers import CargoSerializer

class CargoListCreateView(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class CargoDetailView(generics.RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    lookup_field = 'shipment_id'
