from django.contrib import admin

# Register your models here.
from .models import Movie, Person, Role


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','year','rating','runtime','website',
                    ]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','born','died']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['movie','person','name']