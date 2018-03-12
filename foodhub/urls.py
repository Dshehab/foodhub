"""foodhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurants import views
from django.conf import settings
from django.conf.urls.static import static
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants_list/', views.list, name="go_back"),
    path('restaurant_detail/<int:detail_id>/', views.detail, name="restaurant_detail"),
    path('create/', views.create, name="create_restaurant"),
    path('restaurant_update/<int:restaurant_id>/', views.update, name="restaurant_update"),
    path('delete/<int:delete_id>/', views.delete, name="restaurant_delete"),
    path('register/', views.user_register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('favorite_restaurant/<int:restaurant_id/', views.favorite_restaurant, name="favorite_restaurant"),
    path('api/list/', RestaurantListAPIView.as_view()),
    path('api/detail/<int:detail_id>/', RestaurantDetailAPIView.as_view()),
    path('api/delete/<int:restaurant_id>/', RestaurantDeleteAPIView.as_view()),
    path('api/create/', RestaurantCreateAPIView.as_view()),
    path('api/update/<int:restaurant_id>/', RestaurantUpdateAPIView.as_view()),




]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
