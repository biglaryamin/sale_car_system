from django.http.response import HttpResponse
from django.shortcuts import redirect,render
from .forms import *
from .models import *


def show_home_view(request):
    return render(request,"main_app/home.html")




all_id=[]
def buy_car(request):
    form=Person_form(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            if form.cleaned_data['id_code'] in all_id:
                return HttpResponse("You did it before")
            else:
                all_id.append(form.cleaned_data['id_code'])
                form.save()
                return HttpResponse(all_id)

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




def delete_person_view(request):
    all_id=[]
    if request.method=="POST":
        roll_number = request.POST['delete_id_box']
        all_person=Person.objects.all()
        for person in all_person:
            all_id.append(person.id_code)


        obj=Person.objects.filter(id_code=roll_number)
        obj.delete()

        string="object deleted with this id ==> "+str(roll_number)
        return HttpResponse(string)



def logout_view(request):
    return render(request,"registration/logged_out.html")