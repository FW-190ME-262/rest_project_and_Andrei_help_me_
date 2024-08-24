# python

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class PlanesAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Planes!"})


# Create your views here.

#
def home(request):
    return render(request, 'home.html')
