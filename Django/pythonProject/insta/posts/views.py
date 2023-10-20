from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import CommentForm
# Create your views here.
def feeds(request):
    if not request.user.is_authenticated:
        return redirect("/users/login/")

    user = request.user
    if not user.is_authenticated:
        return redirect("users:login")

    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        "posts": posts,
        "comment_form": comment_form,
    }
    return render(request, "posts/feeds.html", context)