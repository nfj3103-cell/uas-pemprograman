from django.shortcuts import render
from django.shortcuts import render

def dashboard_customer(request):

    return render(
        request,
        "customer/dashboard.html"
        
    )
def home(request):

    return render(
        request,
        "customer/home.html"
    )


def dashboard_customer(request):

    return render(
        request,
        "customer/dashboard.html"
    )