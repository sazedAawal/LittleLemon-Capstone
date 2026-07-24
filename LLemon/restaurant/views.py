from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics, viewsets, permissions, views, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Booking, MenuItem, Menu
from .serializers import BookingSerializer, MenuSerializer, MenuItemSerializer, UserSerializer, RegistrationSerializer


def index(request):
    return render(request, 'index.html', {})

class BookingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data) # Return JSON
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

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


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({'message':'This veiw is protected'})

def about(request):
    return render(request, 'about.html', {})

def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {'menu':menu_data})

def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    return render(request,'menu-item.html', {'menu_item':menu_item})

def book(request):
    return render(request, 'book.html', {})