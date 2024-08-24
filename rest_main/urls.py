# python


from django.urls import path, include
from .views import home
from .views import PlanesAPIView




urlpatterns = [
    path("planes/",PlanesAPIView.as_view(), name='airline_brands'),
]