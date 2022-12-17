from rest_framework.views import APIView, Response
from django.shortcuts import get_object_or_404

from .models import Movie
from .serializers import MovieSerializer

class ListMovieView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serialized_movies = MovieSerializer(movies, many=True)

        return Response(serialized_movies.data)

class RetrieveMovieView(APIView):
    def get(self, request, movie_id=''):
        movie = get_object_or_404(Movie, id=movie_id)
        serialized_movie = MovieSerializer(movie)
        
        return Response(serialized_movie.data)