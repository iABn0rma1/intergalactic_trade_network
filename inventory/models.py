from django.db import models

class Inventory(models.Model):
    station_id = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.station_id} - {self.item}"
