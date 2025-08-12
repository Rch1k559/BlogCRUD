# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings

# Models are Python classes that represent tables in the database.
# Each model corresponds to a single table, and each attribute of the model corresponds to a column in that table.

class Blog(models.Model):
    """
    Model representing a blog post.
    """
    # Field for the post title. CharField is a text field for short strings.
    title = models.CharField("Title", max_length=80)
    
    # Field for the main content of the post. TextField is for long text.
    content = models.TextField("Content")
    
    # Field for the date and time of post creation.
    # default=timezone.now sets the current time by default when a new post is created.
    blog_date = models.DateTimeField("Date Created", default=timezone.now)
    
    def __str__(self):
        """
        String representation of the model object.
        In the Django admin, posts will be displayed by their titles.
        """
        return self.title
        
    class Meta:
        """
        Inner class for model configuration.
        """
        # Singular name of the model for the admin panel.
        verbose_name = "Blog"
        # Plural name of the model.
        verbose_name_plural = "Blogs"
        
class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    """
    # ForeignKey creates a many-to-one relationship.
    # Each comment is linked to a single blog post.
    # on_delete=models.CASCADE means that if a blog post is deleted, all its comments will be deleted as well.
    # related_name='comments' allows accessing comments from a blog object, e.g., blog.comments.all().
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', verbose_name='Blog Post')
    
    # Link to the user who wrote the comment.
    # settings.AUTH_USER_MODEL refers to the default User model in Django.
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Author')
    
    # Field for the comment text.
    text = models.TextField("Comment Text")
    
    # Field for the date and time of comment creation.
    # auto_now_add=True automatically sets the current time when a comment is created.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    
    def __str__(self):
        """
        String representation of the comment object.
        """
        return f"Comment by {self.owner} on {self.blog}"
    
    class Meta:
        """
        Inner class for model configuration.
        """
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        
        # ordering = ['-created_at'] ensures that comments are sorted by creation date in descending order (newest first).
        ordering = ['-created_at']
