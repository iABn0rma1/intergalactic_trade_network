import json
from channels.generic.websocket import AsyncWebsocketConsumer
from trades.models import Trade
from cargo.models import Cargo
from inventory.models import Inventory

class AnalyticsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Fetch data for analytics
        trade_volume = Trade.objects.count()
        active_shipments = Cargo.objects.filter(status='In Transit').count()
        inventory_levels = Inventory.objects.aggregate(total=sum('quantity'))

        # Send data to WebSocket
        await self.send(text_data=json.dumps({
            'trade_volume': trade_volume,
            'active_shipments': active_shipments,
            'inventory_levels': inventory_levels['total'],
        }))
