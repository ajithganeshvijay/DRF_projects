"""
URL configuration for movie_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from movies import views

router=DefaultRouter() #1
router.register('movies',views.MovieView) #2


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("allmovies",views..as_view()),
    # path("moviecreate",views.MovieCreate.as_view()),
    # path('moviedetail/<int:pk>',views.MovieDetail.as_view()),
    # path('movieupdate/<int:pk>',views.MovieUpdate.as_view()),
    # path("moviedelete/<int:pk>",views.MovieDelete.as_view())

    # path("allmovies",views.MovieList.as_view()),
    # path('moviesretreiveupdatedestroy/<int:pk>',views.MovieRetrieveUpdateDelete.as_view()),
    path('searchmovies',views.SearchAPIView.as_view()),
    path('',include(router.urls)) ,#3 ,,
    path('register',views.RegisterAPIView.as_view()),
    # path('login',views.Obtain_Auth_Token.as_view()),
    path('login',obtain_auth_token),
    path('Logout',views.LogoutAPIView.as_view())]
