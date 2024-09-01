from django.db import models

class Trade(models.Model):
    id = models.AutoField(primary_key=True)
    trade_volume = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trade {self.id} - Volume: {self.trade_volume}"

class CargoShipment(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Shipment {self.id} - Status: {self.status}"

class Inventory(models.Model):
    station_id = models.IntegerField()
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Station {self.station_id} - Item: {self.item} - Quantity: {self.quantity}"
