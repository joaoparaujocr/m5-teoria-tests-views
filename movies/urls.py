from django.urls import path
from .views import ListMovieView, RetrieveMovieView

urlpatterns = [
    path('movies/', ListMovieView.as_view()),
    path('movies/<int:movie_id>/', RetrieveMovieView.as_view())
]