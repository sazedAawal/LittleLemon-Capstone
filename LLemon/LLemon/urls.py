from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views
from LittleLemonAPI import views as api_views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'tables', views.BookingViewSet, basename='tables')

router.register(r'users', api_views.UserViewSet, basename='test-user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    #path('restaurant/menu/', include('restaurant.urls')),
    #path('restaurant/booking/', include(router.urls)),
    path('api/', include('restaurant.urls')), 
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/',include('LittleLemonAPI.urls')),
]
