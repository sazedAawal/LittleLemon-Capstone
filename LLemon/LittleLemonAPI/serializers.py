from rest_framework import serializers
from .models import LLAPIMenuItem
from django.contrib.auth.models import User


class LLAPIMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LLAPIMenuItem
        fields = ['id','title','price','inventory',]

class TestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','groups',]