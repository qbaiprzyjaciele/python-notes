from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner")


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("Some info about me")
