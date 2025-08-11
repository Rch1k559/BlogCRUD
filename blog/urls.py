# -*- coding: utf-8 -*-
from django.urls import path
from . import views

# This file defines the URL patterns for the 'blog' application.
# These patterns were included in the main urls.py file of the project.

urlpatterns = [
    # URL for the list of posts. The empty path '' corresponds to the application's root.
    # `views.blog_list` is the view function that will be called.
    # `name='blog_list'` is the name of the route, which can be used for reverse URL resolution in templates and views.
    path('', views.blog_list, name='blog_list'),
    
    # URL for the detailed view of a single post.
    # `<int:pk>` is a "path converter". It matches an integer and passes it
    # as the `pk` argument to the `views.blog_detail` view function.
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    
    # URL for the page to add a new post.
    path('add/', views.blog_add, name='blog_add'),
    
    # URL for the page to edit a post.
    path('<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    
    # URL to delete a post.
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]