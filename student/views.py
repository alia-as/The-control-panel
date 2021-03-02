from django.shortcuts import render , redirect, HttpResponse
from .models import student
from django.contrib.auth.models import User , Group , Permission
# Create your views here.
# teacher = Group.objects.get_or_create(name="teacher" )
#
# students = Group.objects.get_or_create(name="students")
def add_student(request, *args, **kwargs):
    stud = stu_add_form()
    if request.method == "POST":
        stud = stu_add_form(request.POST)
        if stud.is_valid():
            try:
                s = User.objects.create_user(stud["username"].value() , password=stud["password"].value() , first_name = stud["first_name"].value())
                s.save()
                return redirect('/add-student/')
            except:
                return HttpResponse('<h1>We have this guy!!</h1>'
                                    '<a href="/add-student/"> turn back </a>')
        else:
            print(stud.errors)
    return render(request,"addstu_temp.html", {"form" : stud})