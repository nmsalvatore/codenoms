from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-updated_on')
    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, "blog/post_detail.html", context)
