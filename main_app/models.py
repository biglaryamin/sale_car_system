from django.db import models
from django.db.models import aggregates




class Person(models.Model):
    first_name =models.CharField(max_length=50)
    last_name  =models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    age        =models.IntegerField()
    id_code    =models.IntegerField()


    def __str__(self):
        name=self.first_name+" "+self.last_name
        return name



class Car(models.Model):
    car_name=models.CharField(max_length=50)
    car_id  =models.IntegerField()
    color   =models.CharField(max_length=10)


    def __str__(self):
        return self.car_name