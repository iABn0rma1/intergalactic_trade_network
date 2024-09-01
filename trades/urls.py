from django.urls import path
from .views import TradeListCreateView, TradeDetailView, RealTimeUpdatesView

urlpatterns = [
    path('trades/', TradeListCreateView.as_view(), name='trade-list-create'),
    path('trades/<str:transaction_id>/', TradeDetailView.as_view(), name='trade-detail'),
    path('updates/real-time/', RealTimeUpdatesView.as_view(), name='real-time-updates'),
]
