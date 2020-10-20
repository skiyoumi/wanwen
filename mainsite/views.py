from django.shortcuts import render
from dao import neo_4j
from django.http.response import HttpResponse
import json

# Create your views here.
def index(request):
    list = neo_4j.main()
    return render(request, "index.html",{'data':list})






