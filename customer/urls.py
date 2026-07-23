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

]