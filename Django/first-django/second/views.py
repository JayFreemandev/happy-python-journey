from django.shortcuts import render
from second.models import Post
from second.forms import PostForm
from django.http import HttpResponseRedirect

# Create your views here.
def list(reqeust):
    context = {"items": Post.objects.all()}
    return render(reqeust, "second/list.html", context)


def create(request):
    form = PostForm()
    return render(request, "second/create.html", {"form": form})

def confirm(request):
    form = PostForm(request.POST)
    if form.is_valid():
            return render(request, "second/confirm.html", {"form": form})
    return HttpResponseRedirect('/create/')