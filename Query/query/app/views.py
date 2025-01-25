from django.shortcuts import render
from app.models import Student

def alldata(request):
    data=Student.objects.all()
    print(data)

def filterdata(request):
    data=Student.objects.filter(stu_name="Bhoopendra")
    print(data)


def value(request):
    data=Student.objects.values()
    print(data)


def vlist(request):
    data=Student.objects.values_list()
    print(data)

def ex(request):
    data=Student.objects.exclude(stu_name='neeraj')
    print(data)    
