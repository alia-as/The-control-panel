from django.shortcuts import render
from .models import student
from .forms import stu_add_form
# Create your views here.

def add_student(request, *args, **kwargs):
    stu = stu_add_form()
    if request.method == "POST":
        stu = stu_add_form(request.POST)
        if stu.is_valid():
            stu.save()
            stu = stu_add_form()
        else:
            print(stu.errors)
    return render(request,"addstu_temp.html", {"form" : stu})