from django.urls import path
from .views import Home,Search

urlpatterns=[
      path("",Home,name="home"),
      path("search",Search,name="search")
]