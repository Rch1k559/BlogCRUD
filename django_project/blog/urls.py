# -*- coding: utf-8 -*-
from django.urls import path
from . import views

# This file defines the URL patterns for the 'blog' application.
# These patterns are included in the main urls.py file of the project.

# urlpatterns is a list of URL patterns for this application.
# Django searches through this list to find a matching URL.
urlpatterns = [
    # URL for the list of posts. The empty path '' corresponds to the root of this app.
    # `views.blog_list` is the view function that will be called when this URL is accessed.
    # `name='blog_list'` is the unique name for this URL pattern, used for reverse URL lookups.
    path('', views.blog_list, name='blog_list'),
    
    # URL for the detailed view of a single post.
    # `<int:pk>` is a path converter. It matches an integer in the URL
    # and passes it as a keyword argument `pk` to the `views.blog_detail` view.
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    
    # URL for the page to add a new post.
    path('add/', views.blog_add, name='blog_add'),
    
    # URL for the page to edit an existing post, identified by its primary key (pk).
    path('<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    
    # URL to delete a post, identified by its primary key (pk).
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]
