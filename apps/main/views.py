from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Trip
import datetime

def mainindex(request):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    myid = request.session["id"]
    mydate = Trip.objects.get(id=1).start
    context = {
        "this_user": User.objects.get(id=myid),
        "my_trips": Trip.objects.filter(host=myid).order_by("-created_at"),
        "other_trips": Trip.objects.exclude(attendees=myid).exclude(host=myid).order_by("-created_at"),
        "joined_trips": Trip.objects.filter(attendees=myid).order_by("-created_at"),
    }
    print(str(datetime.date.today()))
    print(str(mydate))
    return render(request, "main/index.html", context)

#View Trip
def read(request, id):
    readid = id
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    trip_id =  Trip.objects.get(id=id)
    context = {
        "thetrip": Trip.objects.get(id=readid),
        "going": trip_id.attendees.all(),
    }
    print(id)
    return render(request, "main/viewpage.html", context)

#Trip Creation Page
def pagecreate(request):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    return render(request, "main/pagecreate.html")

#Creates Trips
def create(request, id):
    if request.method == "POST":
        hostid = int(id)
        print(id)
        if "name" not in request.session and request.session["id"] != hostid:
            messages.error(request, 'You can not do that') 
            return redirect("/")
        errors = Trip.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/trips/new")
        de = request.POST["dest"]
        st = request.POST["start"]
        ed = request.POST["end"]
        pl = request.POST["plan"]
        user = User.objects.get(id=hostid)
        Trip.objects.create(destination=de, start=st, end=ed, plan=pl, host=user)
        print(request.POST)
        return redirect("/dashboard")

#Trip Edit Page
def editpage(request, id):
    tripid = int(id)
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    context = {
        "trip": Trip.objects.get(id=tripid),
    }
    return render(request, "main/editpage.html", context)

#Edit trip
def update(request, id):
    if request.method == "POST":
        hostid = int(id)
        print(id)
        if "name" not in request.session and request.session["id"] != hostid:
            messages.error(request, 'You can not do that') 
            return redirect("/")
        errors = Trip.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/trips/edit/"+id)
        de = request.POST["dest"]
        st = request.POST["start"]
        ed = request.POST["end"]
        pl = request.POST["plan"]
        tripid = request.POST["tripid"]
        trip = Trip.objects.get(id=tripid)
        trip.destination = de
        trip.start = st
        trip.end = ed
        trip.plan = pl
        trip.save()
        print(request.POST)
        return redirect("/dashboard")

#join
def join(request, id):
    hostid = int(id)
    if "name" not in request.session and request.session["id"] != hostid:
        messages.error(request, 'You can not do that') 
        return redirect("/")
    userid = request.session["id"]
    user1 = User.objects.get(id=userid)
    trip = Trip.objects.get(id=id)
    trip.attendees.add(user1)
    return redirect("/dashboard")

def delete(request, id, tripid):
    hostid = int(id)
    trip =int(tripid)
    if "name" not in request.session and request.session["id"] != hostid:
        messages.error(request, 'You can not do that') 
        return redirect("/")
    delete = Trip.objects.get(id=trip).delete()
    print(trip)
    return redirect("/dashboard")




# def temp(request):
#     if "id" not in request.session:
#         messages.error(request, 'You must be logged in to access that information') 
#         return redirect("/")
#     context = {
#         "this_user": User.objects.get(id=request.session["id"]),
#     }
#     return render(request, "main/index.html")
