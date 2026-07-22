from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request,user)


            if user.role == "ADMIN":
                return redirect("/admin-dashboard/")


            elif user.role == "PETUGAS":
                return redirect("/petugas/")


            else:
                return redirect("/")


    return render(
        request,
        "registration/login.html"
    )



def logout_view(request):

    logout(request)

    return redirect("/login/")