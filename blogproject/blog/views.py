from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

# View all blog posts
def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

# View a single blog post
def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})

# Create a new blog post
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_create.html', {'form': form})

# Edit an existing blog post
def blog_edit(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blog_edit.html', {'form': form})

# Delete a blog post
def blog_delete(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.delete()
    return redirect('blog_list')
