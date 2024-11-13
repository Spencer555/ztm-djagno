from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello World')


def about(request):
    return HttpResponse('Hi am spencer and there would never be another one')


def hello(request, first_name):
    return HttpResponse(f"Hello there {first_name}")


def add(request, num1, num2):
    return HttpResponse(f'sum = {int(num1) + int(num2)}')