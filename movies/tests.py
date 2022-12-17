from rest_framework.test import APITestCase
from movies.models import Movie
from movies.serializers import MovieSerializer
from django.urls import reverse


class MoviesViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movies = [Movie.objects.create(title=f'Movie {movie_id}') for movie_id in range(1, 6)]
        cls.base_url = reverse('list-movies')

    def test_can_list_all_movies(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
      
        self.assertEqual(len(self.movies), len(response.data))

        for movie in self.movies:
            self.assertIn(
                MovieSerializer(instance=movie).data,
                response.data
            )

    def test_can_retrieve_a_specific_movie(self):
        movie = self.movies[0]
        response = self.client.get(f'{self.base_url}{movie.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], movie.id)

        self.assertEqual(
            MovieSerializer(instance=movie).data,
            response.data
        )

    def test_id_invalid(self):
        response = self.client.get(f'${self.base_url}3435/')
        self.assertEqual(response.status_code, 404)
