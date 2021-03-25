from rest_framework import serializers

from .models import Movie, Person


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id','title','plot','year','rating','runtime','website','director',
                  'writers','actors',)

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id','first_name','last_name','born','died')