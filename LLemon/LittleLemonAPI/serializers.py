from rest_framework import serializers
from .models import LLAPIMenuItem

class LLAPIMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LLAPIMenuItem
        fields = ['id','title','price','inventory',]