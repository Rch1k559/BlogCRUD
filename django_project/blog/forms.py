# -*- coding: utf-8 -*-
from django import forms
from .models import Blog, Comment

# Forms in Django provide a way to create HTML forms,
# validate submitted data, and process it.

class BlogForm(forms.ModelForm):
    """
    ModelForm is a helper class that lets you create a Form class
    from a Django model. This avoids duplicating field definitions.
    """
    class Meta:
        """
        The inner Meta class specifies the model to which the form is linked
        and which fields from that model to include in the form.
        """
        # Specifies that this form is associated with the `Blog` model.
        model = Blog
        # A list of fields from the `Blog` model to be included in the form.
        # Fields like 'blog_date' and 'id' are not included as they are handled automatically.
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    """
    A form for creating a new comment, linked to the Comment model.
    """
    class Meta:
        """
        Configuration for the CommentForm.
        """
        # Specifies that this form is associated with the `Comment` model.
        model = Comment
        # Includes only the 'text' field in the form.
        fields = ['text']
        # The `widgets` dictionary allows customizing the HTML rendering of form fields.
        widgets = {
            # Here, the 'text' field is rendered as a <textarea> HTML element.
            # `attrs` specifies the HTML attributes for this element.
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Leave your comment...'}),
        }
