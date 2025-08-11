# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

# Views are functions or classes that take a web request and return a web response.
# The response can be an HTML page, a redirect, a 404 error, an XML document, an image, etc.

def index(request):
    """
    View for the main page (if it exists).
    In this case, it just renders the index.html template.
    """
    return render(request, 'blog/index.html')

def blog_list(request):
    """
    View to display a list of all blog posts.
    """
    # Gets all objects (posts) from the Blog model.
    blogs = Blog.objects.all()
    # Renders the 'blog/blog_list.html' template and passes the list of posts to it.
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    """
    View to display a single specific blog post.
    `pk` (primary key) is the unique identifier of the post.
    """
    # Tries to find a blog post by its pk. If the post is not found, returns a 404 error.
    blog = get_object_or_404(Blog, pk=pk)
    # Renders the 'blog/blog_detail.html' template and passes the found post to it.
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def blog_add(request):
    """
    View to add a new blog post.
    """
    # If the request was sent by POST (i.e., the user filled out and submitted the form).
    if request.method == 'POST':
        # Creates a form instance and populates it with data from the request.
        form = BlogForm(request.POST)
        # Checks if the data in the form is valid.
        if form.is_valid():
            # Saves the data from the form to the database (creates a new post).
            form.save()
            # Redirects the user to the page with the list of all posts.
            return redirect('blog_list')
    # If the request was by GET (i.e., the user just visited the page).
    else:
        # Creates an empty form instance.
        form = BlogForm()
    # Renders the 'blog/blog_add.html' template and passes the form to it.
    return render(request, 'blog/blog_add.html', {'form': form})

def blog_edit(request, pk):
    """
    View to edit an existing blog post.
    """
    # Finds the post to edit or returns 404.
    blog = get_object_or_404(Blog, pk=pk)
    # If the user submitted the form.
    if request.method == 'POST':
        # Creates a form instance, populating it with data from the request and binding it to the existing post.
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    # If the user just visited the page.
    else:
        # Creates a form instance, pre-filled with data from the existing post.
        form = BlogForm(instance=blog)
    # Renders the editing template, passing the form and the post itself to it.
    return render(request, 'blog/blog_edit.html', {'form': form, 'blog': blog})

def blog_delete(request, pk):
    """
    View to delete a blog post.
    """
    # Finds the post to delete or returns 404.
    blog = get_object_or_404(Blog, pk=pk)
    # Deletion usually happens via a POST request for security.
    if request.method == 'POST':
        # Deletes the post from the database.
        blog.delete()
        # Redirects to the list of posts.
        return redirect('blog_list')
    # If it's a GET request, a confirmation page is displayed.
    return render(request, 'blog/blog_delete.html', {'blog': blog})
