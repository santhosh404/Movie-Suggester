from django.urls import path, include
from . import views

from django.urls import path, include



urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    path('ratedmovies', views.rated_movies, name="rated"),
    path('logout', views.logout, name="logout"),
    path('accounts/', include('allauth.urls')),

]