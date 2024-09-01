from django.urls import path
from .views import CargoListCreateView, CargoDetailView

urlpatterns = [
    path('cargo/', CargoListCreateView.as_view(), name='cargo-list-create'),
    path('cargo/<str:shipment_id>/', CargoDetailView.as_view(), name='cargo-detail'),
]
