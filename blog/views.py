# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

from blog.forms import PostForm
from blog.models import Post, Comment


def is_superuser(user):
    return user.is_superuser


def home(request):
    posts = Post.objects.all()
    user = request.user
    return render(request, 'home.html', {'posts': posts, 'user': user})


@user_passes_test(is_superuser)
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home/')
    else:
        form = PostForm()
    return render(request, 'create-post.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'post-detail.html', {'post': post})
