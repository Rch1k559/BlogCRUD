# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Models are Python classes that represent tables in the database.
# Each model corresponds to a single table, and each attribute of the model corresponds to a column in that table.

class Blog(models.Model):
    """
    Model to represent a blog post.
    """
    # Field for the post title. CharField is a text field for short strings.
    title = models.CharField("Title", max_length=80)
    
    # Field for the main content of the post. TextField is for long texts.
    content = models.TextField("Content")
    
    # Field for the date and time the post was created.
    # default=timezone.now sets the current time by default when a new post is created.
    blog_date = models.DateTimeField("Date Created", default=timezone.now)
    
    def __str__(self):
        """
        A magic method that defines how a model object will be represented as a string.
        For example, in the Django admin panel, posts will be displayed by their titles.
        """
        return self.title
        
    class Meta:
        """
        An inner class for configuring model metadata.
        """
        # The singular name of the model, which will be displayed in the admin panel.
        verbose_name = "Blog"
        # The plural name of the model.
        verbose_name_plural = "Blogs"
