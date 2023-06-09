from django.urls import path

from . import views



app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<slug:slug>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<slug:slug>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<slug:slug>/vote/", views.vote, name="vote"),
]