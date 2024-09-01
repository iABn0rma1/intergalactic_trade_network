from django.db import models

class Trade(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    buyer = models.CharField(max_length=100)
    seller = models.CharField(max_length=100)
    goods = models.JSONField()  # {"item": "Iron", "quantity": 100}
    status = models.CharField(max_length=20, default='Initiated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction_id
