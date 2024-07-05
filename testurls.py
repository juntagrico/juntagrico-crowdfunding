"""
test URL Configuration for juntagrico_crowdfunding development
"""
from django.urls import include, path
from django.contrib import admin
import juntagrico

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('juntagrico.urls')),
    path('', include('juntagrico_crowdfunding.urls')),
]
