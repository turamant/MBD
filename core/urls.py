from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import MovieViewSet,PersonViewSet

app_name = 'core'

router = SimpleRouter()

router.register('movie',MovieViewSet, basename='movie'),
router.register('pers',PersonViewSet, basename='person'),

urlpatterns = [
    path('movies/',views.MovieList.as_view(), name='MovieList'),
    path('movies/<int:pk>/',views.MovieDetail.as_view(), name='MovieDetail'),
    path('person/',views.PersonList.as_view(), name='PersonList'),
    path('person/<int:pk>/',views.PersonDetail.as_view(), name='PersonDetail'),
]
urlpatterns+= router.urls