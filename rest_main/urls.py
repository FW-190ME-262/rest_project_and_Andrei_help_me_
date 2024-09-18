

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import home
from .views import PlanesAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PlanesModelView
router = DefaultRouter()
router.register(r'planes', PlanesModelView)
urlpatterns = [
    path("plane/", PlanesAPIView.as_view(), name='airline_brands'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]


