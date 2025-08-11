# -*- coding: utf-8 -*-
from django import forms
from .models import Blog

# Forms in Django provide a way to create HTML forms,
# validate them, and process the data.

class BlogForm(forms.ModelForm):
    """
    ModelForm is a special form class that is automatically
    generated based on a Django model.
    This saves you from having to manually define the form fields if they
    correspond to the model fields.
    """
    class Meta:
        """
        The inner Meta class specifies which model the form should be based on
        and which fields from that model should be included in the form.
        """
        # Specifies that this form is associated with the `Blog` model.
        model = Blog
        # A list of fields from the `Blog` model that should be in the form.
        # The 'blog_date' and 'id' fields are not included as they are managed automatically.
        fields = ['title', 'content']