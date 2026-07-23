from django.urls import path
from . import views


urlpatterns = [

    path(
        "dashboard-customer/",
        views.dashboard_customer,
        name="dashboard_customer"
    ),

]