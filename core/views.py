from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Movie, Person


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