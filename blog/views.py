from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_home(request):
    # To sort it based on most recent date
    posts = Post.objects.order_by('created_at')
    # posts is a directory coming from above variable passing to view
    return render(request, 'blog/all_home.html', {'posts':posts})