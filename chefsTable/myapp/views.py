from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Welcome to Little Lemon restaurant!")

def say_hello(request):
    return HttpResponse("Hello")

def homepage(request):
    return HttpResponse("Welcome to little lemon!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14"> This is Little Lemon again! </h1>"""
    return HttpResponse(text)