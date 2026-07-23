from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemsViewTest.as_view(), name='menu-items'),
]