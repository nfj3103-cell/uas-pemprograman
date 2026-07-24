from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),


    path(
        "dashboard-customer/",
        views.dashboard_customer,
        name="dashboard_customer"
    ),

    path(
    "event/<int:id>/",
    views.detail_event,
    name="detail_event"
    ),


    path(
    "booking/<int:id>/",
    views.booking_ticket,
    name="booking_ticket"
    ),

]