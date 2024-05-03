from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("dashboard/", include("dashboard.urls")),
    # path("accounts/", include("accounts.urls")),
    # path("blog/", include("blog.urls")),
    path("", home, name="home"),
]
