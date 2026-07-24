from django.urls import path
from . import views
from .views import MenuView, BookingView, RegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-menu/', MenuView.as_view()),
    path('bookings/', BookingView.as_view(), name='bookings'),
    path('api-token-auth/', obtain_auth_token),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('bookings/<int:pk>/', views.SingleBookingView.as_view(), name='booking-detail'),
]