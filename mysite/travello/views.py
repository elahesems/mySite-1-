from django.shortcuts import render

# Create your views here.
from .models import Destination


def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests':dests})





