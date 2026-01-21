from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def home(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reviews:home")
    else:
        form = ReviewForm()

    reviews = Review.objects.filter(verified=True)
    return render(request, "reviews/home.html", {
        "form": form,
        "reviews": reviews,
    })

def about(request):
    return render(request, "reviews/about.html")

def post(request, post_id):
    return render(request, "reviews/post.html", {"post_id": post_id})

def reviews_list(request):
    reviews = Review.objects.filter(verified=True)
    return render(request, "reviews/reviews_list.html", {"reviews": reviews})