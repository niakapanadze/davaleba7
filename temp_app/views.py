from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello!!!!!")

def info(request):
    context = {
        "saxeli": "Nia",
        "gvari": "Kapanadze",
        "asaki": 14,
        "klasi": 9,
        "simagle": 170,
    }
    return render(request, "info.html", context)

def hobbies(request):
    context = {
        "hobbies": ["Watching movies", "Listening to music", "Swimming"],
        "grade": 9,
    }
    return render(request, "hobbies.html", context)