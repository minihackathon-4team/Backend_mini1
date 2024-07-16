from rest_framework import serializers
from .models import *
from django.utils import timezone

class MovieDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = ['movie'] ##################

class ShowPosterTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title_kor', 'title_eng', 'poster_url']

class ShowDetailSerializer(serializers.ModelSerializer):
    actors = ActorDataSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"


class CommentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']

class CommentResponseSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'created_at']

    def get_created_at(self, obj):
        time = timezone.localtime(obj.created_at)
        return time.strftime('%Y-%m-%d')