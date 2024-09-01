from django.db import models

class Cargo(models.Model):
    shipment_id = models.CharField(max_length=100, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    contents = models.JSONField()  # {"item": "Iron", "quantity": 100}
    status = models.CharField(max_length=20, default='In Transit')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shipment_id
