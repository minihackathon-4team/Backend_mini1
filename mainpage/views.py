from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import requests

# Create your models here.

def init_db(request):
    url = "https://port-0-minihackathon-12-lyec0qpi97716ac6.sel5.cloudtype.app/movie"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        data["title_kor"] = movie['title_kor']
        data["title_eng"] = movie["title_eng"]
        data["poster_url"] = movie["poster_url"]
        data["genre"] = movie["genre"]
        data["showtime"] = movie["showtime"]
        data["release_data"] = movie["release_data"]
        data["plot"] = movie["plot"]
        data["rating"] = movie["rating"]
        data["director_name"] = movie["director_name"]
        data["dirctor_image_url"] = movie["dirctor_image_url"]
        serializer = MovieDataSerializer(data)
        if serializer.is_valid():
            serializer.save()
            data={}

        for movie in movies:
            data["name"] = movie["name"]
            data["character"] = movie["character"]
            data["image_url"] = movie["image_url"]
            serializer = ActorDataSerializer(data)
            if serializer.is_valid():
                serializer.save()
                data={}

    return Response(request.data, status=status.HTTP_200_OK)


class MovieList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    def get(self, request):
        movies = Movie.objects.all()
        serializer = ShowPosterTitleSerializer(movies, many=True)
        return Response(serializer.data)

