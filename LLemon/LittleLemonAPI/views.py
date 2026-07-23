from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import LLAPIMenuItem
from .serializers import LLAPIMenuItemSerializer
from django.contrib.auth.models import User

# Create your views here.
class MenuItemsViewTest(generics.ListCreateAPIView):
    queryset = LLAPIMenuItem.objects.all()
    serializer_class = LLAPIMenuItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    query_set = User.objects.all()