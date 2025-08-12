# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Blog, Comment

# This file is used to configure how your models are displayed
# and managed in the Django admin interface.

# The simplest way to make a model visible in the admin is to register it.
# `admin.site.register(Blog)` makes the `Blog` model available in the admin panel.
# This allows creating, reading, updating, and deleting blog posts via the admin UI.
admin.site.register(Blog)

# Similarly, this registers the `Comment` model in the admin panel.
admin.site.register(Comment)
