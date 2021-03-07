from django.shortcuts import render , redirect, HttpResponse
from .models import student
from django.contrib.auth.models import User , Group , Permission
from .forms import stu_add_form
from django.views.generic import TemplateView
# Create your views here.
# teacher = Group.objects.get_or_create(name="teacher" )
#
# students = Group.objects.get_or_create(name="students")
try:
    User.objects.create_superuser("ali" , first_name="ali" ,last_name = "aa" , password="aa@123456"  , email="abdollahi.ali@ut.ac.ir")
except: pass
try:
    User.objects.create_user("abbas" , password="an@123456" , first_name = "abbas" , last_name= "nowzari" , email="nowzari@ut.ac.ir")
except: pass
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
class profile(TemplateView):
    template_name = "profile.html"
