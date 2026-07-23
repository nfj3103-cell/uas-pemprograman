from django.shortcuts import render


def dashboard_customer(request):

    return render(
        request,
        "customer/dashboard.html"
    )