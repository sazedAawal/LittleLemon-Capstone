from django.urls import path
from . import views

urlpatterns = [
    path('menu-items-test/', views.MenuItemsViewTest.as_view(), name='menu-items-tests'),
]