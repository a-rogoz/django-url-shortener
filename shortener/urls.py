from django.urls import path, re_path

from .views import RedirectShortURLView, ShortURLCreateView

app_name = "shortener"

urlpatterns = [
    path("shorten-url/", ShortURLCreateView.as_view(), name="shorten-url"),
    re_path(
        r"^shrt/(?P<code>[0-9A-Za-z]{6})/$",
        RedirectShortURLView.as_view(),
        name="redirect-short-url",
    ),
]
