import tkinter
import datetime
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request,"home.html",{})

def add_activity(request):
    if request.method=="GET":
        return render(request,"add_details.html",{})

def add_food(request):
    if request.method=="GET":
        return render(request,"add_food.html",{})
    if request.method=="POST":
        fname= request.POST.get("fname")
        ftable = Foodtable(fname=fname)
        ftable.save()
        time= datetime.datetime.now()
        return render(request,"food_added_successfully.html",{"ftable":ftable,"time":time})


def add_exercise(request):
    if request.method == "GET":
        return render(request, "add_exercise.html", {})
    if request.method == "POST":
        ename=request.POST.get("ename")
        etable = Exercisetable(ename=ename)
        etable.save()
        time = datetime.datetime.now()
        return render(request,"exercise_added_successfully.html",{"ename":ename, "time":time})


def read_activity(request):
    if request.method=="GET":
        return render(request,"read_details.html",{})

def read_food(request):
    allFoodName = Foodtable.objects.all()[::-1]
    print(allFoodName)
    time = datetime.datetime.now()
    return render(request, "read_food_list.html", {"allFoodName": allFoodName,"time":time})

def read_exercise(request):
    allExeName= Exercisetable.objects.all()[::-1]
    time = datetime.datetime.now()
    return render(request, "read_exercise_list.html", {"allExeName":allExeName,"time":time})

def delete_food(request, id):
    foodtable = Foodtable.objects.get(id=id)
    foodtable.delete()
    allFoodName = Foodtable.objects.all()
    time = datetime.datetime.now()
    return render(request, "read_food_list.html", {"allFoodName": allFoodName, "time":time} )

def delete_exe(request, id):
    exetable = Exercisetable.objects.get(id=id)
    exetable.delete()
    allExeName = Exercisetable.objects.all()
    time = datetime.datetime.now()
    return render(request, "read_exercise_list.html", {"allExeName": allExeName, "time": time})

def update_food(request,id):
    if request.method == "GET":
        foodtable = Foodtable.objects.filter(id=id).first()
        return render(request, "update_food.html", {"foodtable": foodtable})
    if request.method == "POST":
        foodtable= Foodtable.objects.filter(id=id).first()
        fname = request.POST.get("fname")
        foodtable.fname = fname
        foodtable.save()
        allFoodName = Foodtable.objects.all()
        return render(request,"read_food_list.html",{"allFoodName": allFoodName})

def update_exe(request,id):
    if request.method == "GET":
        exetable = Exercisetable.objects.filter(id=id).first()
        return render(request, "update_exe.html", {"exetable": exetable})
    if request.method == "POST":
        exetable= Exercisetable.objects.filter(id=id).first()
        ename = request.POST.get("ename")
        exetable.ename = ename
        exetable.save()
        allExeName = Exercisetable.objects.all()
        return render(request,"read_exercise_list.html",{"allExeName": allExeName})