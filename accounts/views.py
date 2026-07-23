from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import Profile


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")


    else:

        form = RegisterForm()


    return render(
        request,
        "registration/register.html",
        {
            "form": form
        }
    )



def login_view(request):

    error = None


    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username=email,
            password=password
        )


        if user is not None:

            login(request, user)


            try:

                role = user.profile.role


                if role == "ADMIN":

                    return redirect(
                        "/dashboard-admin/"
                    )


                elif role == "PETUGAS":

                    return redirect(
                        "/dashboard-petugas/"
                    )


                elif role == "CUSTOMER":

                    return redirect(
                        "/dashboard-customer/"
                    )


                else:

                    return redirect("/")


            except Profile.DoesNotExist:

                return redirect("/")


        else:

            error = "Email atau kata sandi salah!"



    return render(
        request,
        "registration/login.html",
        {
            "error": error
        }
    )



def logout_view(request):

    logout(request)

    return redirect("login")