from django.shortcuts import render
from events.models import Event, Booking, Payment, ETicket
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


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

def detail_event(request,id):

    event = get_object_or_404(
        Event,
        id=id
    )


    tickets = Ticket.objects.filter(
        event=event
    )


    return render(
        request,
        "customer/detail_event.html",
        {
            "event":event,
            "tickets":tickets
        }
    )

def booking_ticket(request,id):

    ticket = get_object_or_404(
        Ticket,
        id=id
    )


    if request.method == "POST":


        Booking.objects.create(

            user=request.user,

            ticket=ticket,

            jumlah=1,

            total_harga=ticket.harga

        )


        return redirect(
            "dashboard_customer"
        )


    return redirect(
        "dashboard_customer"
    )