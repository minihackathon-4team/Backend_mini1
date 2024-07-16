from rest_framework import serializers
from .models import *

class MovieDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = ['movie']

class ShowPosterTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title_kor', 'title_eng', 'poster_url']

class ShowDetailSerializer(serializers.ModelSerializer):
    actors = ActorDataSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"

#여기부터 수정
class MovieDetailSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    comments = CommentResponseSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
    