from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ranking", views.ranking, name="ranking"),
    path("champion/<str:champion_name>/", views.champion, name="champion")
]