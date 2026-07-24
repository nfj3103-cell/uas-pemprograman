from django.shortcuts import render
from events.models import Event, Booking, Payment, ETicket


def home(request):

    return render(
        request,
        "customer/home.html"
    )



def dashboard_customer(request):

    user = request.user


    # event yang aktif
    events = Event.objects.filter(
        status="AKTIF"
    )


    # booking milik customer
    bookings = Booking.objects.filter(
        user=user
    )


    # pembayaran customer
    payments = Payment.objects.filter(
        booking__user=user
    )


    # e-ticket customer
    etickets = ETicket.objects.filter(
        booking__user=user
    )


    context = {

        "events": events,

        "bookings": bookings,

        "payments": payments,

        "etickets": etickets,

    }


    return render(
        request,
        "customer/dashboard.html",
        context
    )