from django.core import paginator
from django.shortcuts import render
from django.contrib.auth import authenticate, login as log_in, logout as log_out
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import userForm, RaterForm
from .models import RATING, Rater
from django.core.paginator import Paginator

# Create your views here.


def signup(request):
     # code for signup
    form = userForm()
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "signup.html", {
                "messageforsignup": "Successfully Registered!", "form": form
            })
    return render(request, "signup.html", {
        "form": form
    })


def login(request):
    # code for login
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log_in(request, user)
            return HttpResponseRedirect(reverse('rated'))
        else:
            return render(request, "login.html", {
                "messageforlogin": "Invalid Credential!"
            })
    return render(request, "login.html")


def home(request):
    rater_form = RaterForm()
    if request.method == 'POST':
        print(request.POST)
        rater_form = RaterForm(request.POST)
        print(rater_form)
        if rater_form.is_valid():
            print('HI')
            rater_form.save()
            return HttpResponseRedirect(reverse('rated'))
    return render(request, "home.html", {
        "Name": request.user.username, "rated_form":rater_form
    })


def rated_movies(request):
    rated_movies = Rater.objects.all().order_by('-id')
    
    
    

    if request.method == 'POST':
        movie_name = request.POST['search_movie']
        q = Rater.objects.filter(Movie_Name__startswith=movie_name)

        if len(q) == 0:
            return render(request, 'rated_movies.html', {
                'none_movie':"No Movies Found."
            })
        return render(request, 'rated_movies.html', {"search_movie":q})

    paginator=Paginator(rated_movies, 6)
    page=request.GET.get('page')

    try:
        books=paginator.page(page)
    except:
        books=paginator.page(1)

    return render(request, 'rated_movies.html', {
        "rated_movies":books, "page":page
    })



def logout(request):
    log_out(request)
    return HttpResponseRedirect(reverse('login'))
