from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from trades.views import RealTimeUpdatesView
from .views import api_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('updates/real-time/', RealTimeUpdatesView.as_view(), name='real-time-updates'),
    path('api/', api_index, name='api_index'),
    path('api/', include('trades.urls')),
    path('api/', include('cargo.urls')),
    path('api/', include('inventory.urls')),
    path('analytics/', include('analytics.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
