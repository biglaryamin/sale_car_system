from django.urls import path
from .views import *



app_name="main_app"
urlpatterns = [
    path("home",show_home_view,name="home"),
    path("buy_car_1",buy_car,name="buy_car"),
    path("buy_car_2",Buy_car_view,name="buy_car_2"),
    path("delete",delete_person_view,name="delete_person"),
    path("logout",logout_view,name="logout"),

]
