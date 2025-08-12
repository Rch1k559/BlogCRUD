# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required

# Views are functions or classes that handle a web request and return a web response.
# A response can be an HTML page, a redirect, a 404 error, an XML document, an image, etc.

def index(request):
    """
    View for the main page.
    This view renders the 'index.html' template.
    """
    return render(request, 'blog/index.html')

def blog_list(request):
    """
    View to display a list of all blog posts.
    """
    # Retrieve all blog posts from the database.
    blogs = Blog.objects.all()
    # Render the 'blog_list.html' template, passing the list of blogs to it.
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    """
    View to display a single blog post identified by its primary key (pk).
    Also handles the submission of new comments.
    """
    # Retrieve the blog post with the given pk, or return a 404 error if not found.
    blog = get_object_or_404(Blog, pk=pk)
    
    # Retrieve all comments associated with this blog post.
    comments = blog.comments.all()
    
    # Instantiate an empty comment form.
    comment_form = CommentForm()
    
    # Handle POST request for adding a new comment.
    if request.method == 'POST':
        # Check if the user is authenticated before allowing to post a comment.
        if not request.user.is_authenticated:
            return redirect('login') # Redirect to login page if not authenticated.
        
        # Create a form instance with the submitted data.
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create a new comment object but don't save it to the database yet.
            new_comment = comment_form.save(commit=False)
            # Associate the comment with the current blog post and user.
            new_comment.blog = blog
            new_comment.owner = request.user
            # Save the new comment to the database.
            new_comment.save()
            
            # Redirect to the same blog detail page to display the new comment.
            return redirect('blog_detail', pk=blog.pk)
        
    # Prepare the context to be passed to the template.
    context = {
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form,
    }
    # Render the 'blog_detail.html' template with the blog post and comments.
    return render(request, 'blog/blog_detail.html', context)

@login_required # This decorator ensures that only logged-in users can add a new blog post.
def blog_add(request):
    """
    View to add a new blog post.
    Requires the user to be logged in.
    """
    # Handle POST request for submitting the new blog form.
    if request.method == 'POST':
        # Create a form instance with the submitted data.
        form = BlogForm(request.POST)
        # Validate the form data.
        if form.is_valid():
            # Save the new blog post to the database.
            form.save()
            # Redirect to the list of all blog posts.
            return redirect('blog_list')
    # Handle GET request by displaying an empty form.
    else:
        form = BlogForm()
    # Render the 'blog_add.html' template with the form.
    return render(request, 'blog/blog_add.html', {'form': form})

@login_required # This decorator ensures that only logged-in users can edit a blog post.
def blog_edit(request, pk):
    """
    View to edit an existing blog post.
    Requires the user to be logged in.
    """
    # Retrieve the blog post to be edited, or return a 404 error if not found.
    blog = get_object_or_404(Blog, pk=pk)
    # Handle POST request for submitting the edited blog form.
    if request.method == 'POST':
        # Create a form instance with the submitted data and bind it to the existing blog post.
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            # Save the changes to the blog post.
            form.save()
            # Redirect to the list of all blog posts.
            return redirect('blog_list')
    # Handle GET request by displaying the form pre-filled with the existing blog post data.
    else:
        form = BlogForm(instance=blog)
    # Render the 'blog_edit.html' template with the form and blog post.
    return render(request, 'blog/blog_edit.html', {'form': form, 'blog': blog})

@login_required # This decorator ensures that only logged-in users can delete a blog post.
def blog_delete(request, pk):
    """
    View to delete a blog post.
    Requires the user to be logged in.
    """
    # Retrieve the blog post to be deleted, or return a 404 error if not found.
    blog = get_object_or_404(Blog, pk=pk)
    # Deletion is handled via a POST request for security reasons.
    if request.method == 'POST':
        # Delete the blog post from the database.
        blog.delete()
        # Redirect to the list of all blog posts.
        return redirect('blog_list')
    # For a GET request, display a confirmation page.
    return render(request, 'blog/blog_delete.html', {'blog': blog})
