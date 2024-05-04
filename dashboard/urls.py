from django.urls import path
from .views import dashboard_view, post_edit_view, post_delete_view, post_new_view

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("new/", post_new_view, name="post_new"),
    path("edit/post/<str:slug>/", post_edit_view, name="post_edit"),
    path("delete/post/<str:slug>/", post_delete_view, name="post_delete")
]
