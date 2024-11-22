from django.http import HttpResponse
from django.shortcuts import render

def students(request):
    students = [
        {'id': 101, 'name': 'John dey', 'age': 20}
    ]
    return HttpResponse(students)
