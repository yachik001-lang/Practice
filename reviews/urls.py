from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.home, name="home"),               # Главная (только форма)
    path("about/", views.about, name="about"),       # О блоге
    path("post/<int:post_id>/", views.post, name="post"),  # Страница поста
    path("reviews/", views.reviews_list, name="reviews_list"),  # ← НОВАЯ СТРАНИЦА
]