from django.shortcuts import render
from blog.models import Post


def home(request):
    posts = Post.objects.all().order_by("-updated_on")[:5]
    context = {"posts": posts}
    return render(request, "codenoms/home.html", context)
