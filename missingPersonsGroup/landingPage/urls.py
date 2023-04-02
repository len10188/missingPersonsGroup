# importing urls and setting up path
from django.urls import path
from .views import indexPageView

urlpatterns = [
    path("", indexPageView, name = "index")
]