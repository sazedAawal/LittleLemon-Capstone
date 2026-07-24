from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views
from LittleLemonAPI import views as api_views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

router.register(r'test-users', api_views.UserViewSet, basename='test-user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('router/', include(router.urls)),  
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include('restaurant.api_urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/test/', include('LittleLemonAPI.urls')),
]