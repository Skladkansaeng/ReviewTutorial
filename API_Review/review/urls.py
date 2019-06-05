from django.urls import path

from .views import ReviewView


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('review/', ReviewView.as_view()),
]