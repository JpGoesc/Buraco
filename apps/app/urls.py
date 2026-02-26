from django.urls import path
from . import views

urlpatterns = [
    path("partidas/", views.create_match_api, name="create_match"),
]
