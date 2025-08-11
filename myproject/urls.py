# -*- coding: utf-8 -*-
"""
URL configuration for the myproject project.

The `urlpatterns` list routes URLs to views.
For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

# `urlpatterns` is a list of all URL patterns for the project.
# Django checks each pattern in order and stops at the first match.
urlpatterns = [
    # Route for the Django administrative site.
    # All URLs starting with 'admin/' will be handled by the admin panel.
    path('admin/', admin.site.urls),
    
    # Includes URL patterns from the 'blog' application.
    # All requests to the root URL ('') will be passed to the urls.py file of the 'blog' app.
    path('', include('blog.urls')),
]
