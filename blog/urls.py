from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_home, name='Home'),
    path('<int:blog_id>', views.details, name='Details'),
]