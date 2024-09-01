from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from cargo.models import Cargo
from trades.models import Trade
from inventory.models import Inventory

class AnalyticsDashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard.html')

class RealTimeUpdatesView(View):
    def get(self, request, *args, **kwargs):
        trades = Trade.objects.all()
        cargo_shipments = Cargo.objects.all()
        inventories = Inventory.objects.all()

        # Prepare data for real-time updates
        data = {
            'trades': list(trades.values('id', 'trade_volume', 'timestamp')),
            'cargo_shipments': list(cargo_shipments.values('id', 'status', 'location')),
            'inventories': list(inventories.values('station_id', 'item', 'quantity')),
        }

        return JsonResponse(data)
