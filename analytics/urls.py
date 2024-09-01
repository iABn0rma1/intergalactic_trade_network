from django.urls import path
from .views import AnalyticsDashboardView, RealTimeUpdatesView

app_name = 'analytics'

urlpatterns = [
    path('dashboard/', AnalyticsDashboardView.as_view(), name='dashboard'),
    path('updates/real-time/', RealTimeUpdatesView.as_view(), name='real-time-updates'),
]
