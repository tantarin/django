from django.urls import path
from . import views


urlpatterns = [
    path('test', views.create_post_page),
    path('first', views.first),
    path('home', views.home)
]