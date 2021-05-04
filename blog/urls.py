from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='Home_blog'),
    path('<int:blog_id>', views.details, name='Details'),
]