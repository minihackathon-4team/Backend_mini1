from rest_framework import serializers
from .models import *

class MovieDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class ShowPosterTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title_kor', 'title_eng', 'poster_url']
    