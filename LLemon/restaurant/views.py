from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics, viewsets, permissions, views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuSerializer, MenuItemSerializer, UserSerializer



# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingView(APIView):
    def get(self,request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data) # Return JSON

class MenuView(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 
                            'data':serializer.data})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset= MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset= MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@api_view()
@permission_classes(IsAuthenticated)
def msg(request):
    return Response({'message':'This veiw is protected'})
