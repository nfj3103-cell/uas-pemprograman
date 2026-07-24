from django.shortcuts import render
from events.models import Event, Booking, Payment


def home(request):

    return render(
        request,
        "customer/home.html"
    )


def dashboard_customer(request):

    user = request.user


    # ambil data event
    events = Event.objects.all()


    # ambil booking milik customer
    bookings = Booking.objects.filter(
        user=user
    )


    # ambil pembayaran customer
    payments = Payment.objects.filter(
        booking__user=user
    )


    context = {

        "events": events,

        "bookings": bookings,

        "payments": payments,

    }


    return render(
        request,
        "customer/dashboard.html",
        context
    )