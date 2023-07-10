from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Transport
from .serializers import TransportSerializer


# Create your views here.
class TransportViewSet(ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
