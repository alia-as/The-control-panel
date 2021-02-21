from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args,**kwargs):
    mycontex = {

    }
    return render(request,"home_temp.html",mycontex)
def student_view(request,*args,**kwargs):
    return render(request,"student_temp.html",{})
def teacher_view(request,*args,**kwargs):
    return render(request,"teacher_temp.html",{})
