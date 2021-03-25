from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Movie, Person

from rest_framework import viewsets

from .serializers import MovieSerializer, PersonSerializer


class MovieList(ListView):
    model = Movie
    paginate_by = 10

class PersonList(ListView):
    model = Person
    paginate_by = 10

class MovieDetail(DetailView):
    queryset = Movie.objects.all_with_related_persons()

class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all_with_related_persons()
    serializer_class = MovieSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all_with_prefetch_movies()
    serializer_class = PersonSerializer