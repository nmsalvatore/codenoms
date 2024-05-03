from django.urls import path
from .views import post_list, post_detail

urlpatterns = [
    path("", post_list, name="home"),
    path("post/<str:slug>", post_detail, name="post_detail"),
]
