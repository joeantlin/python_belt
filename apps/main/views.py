from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def mainindex(request):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    context = {
        "this_user": User.objects.get(id=request.session["id"]),
    }
    return render(request, "main/index.html")


def read(request, id):
    readid = id
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    context = {
        "this_user": User.objects.get(id=readid),
    }
    print(id)
    return render(request, "main/index.html")

def create(request, id):
    if request.method == "POST":
        hostid = int(id)
        print(id)
        if "name" not in request.session and request.session["id"] != hostid:
            messages.error(request, 'You can not do that') 
            return redirect("/")
        #temp = request.POST["temp"]
        #user = Temp.objects.get(id=hostid)
        #Class.objects.create(name=temp)
        print(request.POST)
        return redirect("/main")

def update(request, id):
    if request.method == "POST":
        hostid = int(id)
        print(id)
        if "name" not in request.session and request.session["id"] != hostid:
            messages.error(request, 'You can not do that') 
            return redirect("/")
        #temp = request.POST["temp"]
        #user = Temp.objects.get(id=hostid)
        #user.attribute = temp
        print(request.POST)
        return redirect("/main")

def delete(request, id):
    hostid = int(id)
    if "name" not in request.session and request.session["id"] != hostid:
        messages.error(request, 'You can not do that') 
        return redirect("/")
    #delete = Temp.objects.get(id=hostid).delete()
    print(id)
    return redirect("/main")




# def temp(request):
#     if "id" not in request.session:
#         messages.error(request, 'You must be logged in to access that information') 
#         return redirect("/")
#     context = {
#         "this_user": User.objects.get(id=request.session["id"]),
#     }
#     return render(request, "main/index.html")
