from django.urls import path
from django.urls import re_path
from ABSOLUTE import views

urlpatterns = [
path('index', views.index, ),
path(r'^review',views.review ),
path(r'^review_insert', views.review_insert,name="review_insert"),
]