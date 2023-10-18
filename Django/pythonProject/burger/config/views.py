from django.shortcuts import render
from burgers.models import Burger
def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers= Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {
        "burgers" : burgers
    }

    return render(request, "burger_list.html", context)

def burger_search(request):
    keyword = request.GET.get("keyword");
    print(keyword)

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    else:
        burgers = Burger.objects.none()

    context = {
        "burgers" : burgers,
    }
    return render(request, "burger_search.html", context)