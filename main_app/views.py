from django.http.response import HttpResponse
from django.shortcuts import redirect,render
from .forms import *
from .models import *


def show_home_view(request):
    return render(request,"main_app/home.html")





def buy_car(request):
    form=Person_form(request.POST or None)


    all_person=Person.objects.all()
    all_id=[]
    for person in all_person:
        all_id.append(person.last_name)
        
    if request.method == "POST":
        if form.is_valid():
            return HttpResponse(all_id)
            form.save()
            return redirect("main_app:buy_car_2")
            
    context={
        'form':form,
    }
    return render(request,"main_app/buy_car.html",context)




def Buy_car_view(request):
    form=Buy_car_form(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
    context={
        'form':form,
    }
    return render(request,"main_app/buy_car_2.html",context)

