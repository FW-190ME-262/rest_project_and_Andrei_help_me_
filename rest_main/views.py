# python
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Planes
from .serializers import PlanesSerializer


class PlanesAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, Planes! Vari god "})


# Create your views here.

#

def home(request):
    return render(request, "views/home.html")




class MySecureView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    class CarModelViewSet(viewsets.ModelViewSet):
        queryset = Planes.objects.all()
        serializer_class = PlanesSerializer

    def get(self, request):
        return Response(data={"message": "Это защищенное представление!"})


class PlanesModelView(viewsets.ModelViewSet):
    queryset = Planes.objects.all()
    serializer_class = PlanesSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Создать новый самолёт",
        responses={201: openapi.Response('Автомобиль создан', PlanesSerializer), 400: "Ошибка валидации"},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Имя автомобиля'),
                'make': openapi.Schema(type=openapi.TYPE_STRING, description='Марка автомобиля'),
            },
            required=['name', 'make'],
            example={
                "name": "Camry",
                "make": "Toyota",
            }
        )
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)