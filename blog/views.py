# get_object_or_404 used in details function
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def blog_home(request):
    # To sort it based on most recent date
    posts = Post.objects.order_by('created_at')
    # posts is a directory coming from above variable passing to view
    return render(request, 'blog/all_home.html', {'posts':posts})
def details(request, blog_id):
    postId = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/details.html', {'YasObject':postId})