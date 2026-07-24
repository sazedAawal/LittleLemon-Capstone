from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import LLAPIMenuItem
from .serializers import LLAPIMenuItemSerializer, TestUserSerializer
from django.contrib.auth.models import User


class MenuItemsViewTest(generics.ListCreateAPIView):
    queryset = LLAPIMenuItem.objects.all()
    serializer_class = LLAPIMenuItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = TestUserSerializer