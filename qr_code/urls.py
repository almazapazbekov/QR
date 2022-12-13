"""qr_code URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from qr_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('category_create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category_crud/<int:pk>', views.CategoryCrud.as_view(), name='category_crud'),
    path('item_create/', views.ItemCreate.as_view(), name='item_create'),
    path('item_crud/<int:pk>', views.ItemCrud.as_view(), name='item_crud'),

]
