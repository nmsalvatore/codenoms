from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from blog.models import Post
from .forms import PostForm


@login_required
def dashboard_view(request):
    posts = Post.objects.all().order_by('-updated_on')
    context = {'posts': posts}
    return render(request, "dashboard/dashboard.html", context)


@login_required
def post_new_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.content = request.POST.get('content')
            post.slug = slugify(post.title)
            post.is_published = True
            post.save()
        return redirect("dashboard")

    else:
        form = PostForm()
        context = {'form': form}
        return render(request, "dashboard/post_new.html", context)


@login_required
def post_edit_view(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.author = request.user
            updated_post.content = request.POST.get('content')
            updated_post.slug = slugify(updated_post.title)
            updated_post.save()
        return redirect("dashboard")

    else:
        post = Post.objects.get(slug=slug)
        form = PostForm(instance=post)
        context = {'form': form, 'post': post}
        return render(request, "dashboard/post_edit.html", context)


@login_required
def post_delete_view(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    return redirect("dashboard")
