"""
test URL Configuration for juntagrico_crowdfunding development
"""
from django.urls import include, path
from django.contrib import admin
import juntagrico

urlpatterns = [
    path(r'admin', admin.site.urls),
    path(r'', include('juntagrico.urls')),
    path(r'', include('juntagrico_crowdfunding.urls')),
    path(r'', juntagrico.views.home),
]
