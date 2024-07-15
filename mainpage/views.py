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

@api_view(['GET'])
def init_db(request):
    url = "https://port-0-minihackathon-12-lyec0qpi97716ac6.sel5.cloudtype.app/movie"
    res = requests.get(url)
    movies = res.json()['movies']
    data = {}
    data_ = {}
    for movie in movies:
        data["title_kor"] = movie['title_kor']
        data["title_eng"] = movie["title_eng"]
        data["poster_url"] = movie["poster_url"]
        data["genre"] = movie["genre"]
        data["showtime"] = movie["showtime"]
        data["release_date"] = movie["release_date"]
        data["plot"] = movie["plot"]
        data["rating"] = movie["rating"]
        data["director_name"] = movie["director_name"]
        data["director_image_url"] = movie["director_image_url"]
        serializer = MovieDataSerializer(data=data)
        if serializer.is_valid():
            a = serializer.save() # a로 save()된 같은 반환해서

            for actors in movie['actors']:
                data_["name"] = actors["name"]
                data_["character"] = actors["character"]
                data_["image_url"] = actors["image_url"]
                serializer1 = ActorDataSerializer(data=data_)
                if serializer1.is_valid(raise_exception=True):  # raise_exception=True 꼭 넣기   # serializer보면 ActorDataSerializer의 fields를 '__all__'이라 해서 유효성을 통과 못해서 actors 데이터가 저장이 안됨. 왜냐면 model에는 movie가 있는데 movie 데이터를 안 받았기 때문 so, ActorDataSerializer에 movie 필드를 exclude
                    serializer1.save(movie=a) # 1:N 연결 (movie(1):actors(N))
                    data_={}

    return Response(status=status.HTTP_200_OK)


class MovieList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    def get(self, request):
        movies = Movie.objects.all()
        serializer = ShowPosterTitleSerializer(movies, many=True)
        return Response(serializer.data)

class MovieDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get_object(self, pk):
        movie = get_object_or_404(Movie, pk=pk)
        return movie

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = ShowDetailSerializer(movie, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

