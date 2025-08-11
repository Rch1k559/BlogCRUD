# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Blog

# This file is used to configure how your models are
# displayed and work in the Django administrative interface.

# `admin.site.register(Blog)` registers the `Blog` model in the admin panel.
# After this, you will be able to create, view, edit, and delete
# blog posts through the standard Django administrator interface.
admin.site.register(Blog)