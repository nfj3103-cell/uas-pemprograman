from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')


    else:

        form = RegisterForm()


    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )



def login_view(request):

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']


        user = authenticate(
            request,
            username=email,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect('/')


    return render(
        request,
        'registration/login.html'
    )



def logout_view(request):

    logout(request)

    return redirect('login')