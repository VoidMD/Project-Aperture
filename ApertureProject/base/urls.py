from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerPage, name="register"),
    path('profile/',views.userProfile, name="profile"),
    path('FlightSearch/',views.flight_search, name="flight_search"),
    path('ManageBooking/',views.manage_booking, name="manage_booking"),
    path('CheckIn/',views.check_in, name="check_in"),

]