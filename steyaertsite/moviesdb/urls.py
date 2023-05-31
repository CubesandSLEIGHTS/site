from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("db/", views.db, name='db'),
    path("add/", views.add, name='add'),
    path("g/", views.g, name='g'),
    path("pg/", views.pg, name='pg'),
    path("pg13/", views.pg13, name='pg13'),
    path("r/", views.r, name='r'),
    path("nr/", views.nr, name='nr'),
    path("tv/", views.tv, name='tv'),
    path("search/", views.search, name='search'),
    path("results/", views.search_results, name='searchRes'),
]