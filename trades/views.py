from rest_framework import generics
from .models import Trade
from .serializers import TradeSerializer

class TradeListCreateView(generics.ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

class TradeDetailView(generics.RetrieveAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    lookup_field = 'transaction_id'

from django.http import JsonResponse
from django.views import View
from trades.models import Trade
from cargo.models import Cargo

class RealTimeUpdatesView(View):
    def get(self, request):
        # Fetch all trades and cargo shipments
        trades = Trade.objects.all().values('transaction_id', 'buyer', 'seller', 'goods', 'status', 'created_at')
        cargo_shipments = Cargo.objects.all().values('shipment_id', 'origin', 'destination', 'contents', 'status', 'created_at')

        # Prepare the response data
        data = {
            'trades': list(trades),
            'cargo_shipments': list(cargo_shipments)
        }

        return JsonResponse(data, status=200)
