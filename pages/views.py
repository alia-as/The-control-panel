from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args,**kwargs):
    return HttpResponse("<h1>That's awesome</h1>")
def student_view(request,*args,**kwargs):
    return HttpResponse("<h1>Hi Students</h1>")
def teacher_view(request,*args,**kwargs):
    return HttpResponse("<h1>Hello Mr. Nowzari</h1>")