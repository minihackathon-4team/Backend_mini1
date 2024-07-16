from django.urls import path, include
from .views import *

app_name = 'mainpage'

urlpatterns = [
    path('', MovieList.as_view()),
    path('detail/<int:pk>/', MovieDetail.as_view()),
    path('db/', init_db),
    path('comment/<int:pk>/', CommentDetail.as_view())
]