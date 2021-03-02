from django.shortcuts import render , get_object_or_404
from .forms import exercise_form_tea,exercise_form_tea_grade , exercise_form_stu
from .models import exercise
from django import forms
# Create your views here.

def stu_exercises(request , *args,**kwargs):
    all_exer = exercise.objects.all()
    return render(request,"stexer_temp.html",{"all" : all_exer})
def stu_upload_view(request , id , *args , **kwargs):
    exercise_file = forms.CharField(max_length=100)
    #ex = exercise.objects.get(id=id)
    if request.method == "POST":

        print("Tryiiiiiiiiiiiiiing")
        print("Foooooooooooooooooooorms",exercise_file)
    return render(request, "exer_upload_temp.html", {'form' : exercise_file})
def tea_add_exer_view(request,*args,**kwargs):
    exer = exercise_form_tea()
    if request.method == "POST":
        exer = exercise_form_tea(request.POST)
        if exer.is_valid():
            exer.save()
            exer = exercise_form_tea()
        else:
            print('Errors :\t',exer.errors)
    return render(request,"texer_add_temp.html",{'form' : exer})
def tea_exercises(request,*args,**kwargs):
    all_exer = exercise.objects.all()
    return render(request, "texer_temp.html", {"all": all_exer})
def exercise_stu_view(request , id , *args , **kwargs):
    ex = exercise.objects.get(id=id)
    return render(request,"exers_stu_temp.html",{'exercise' : ex})
def exercise_tea_view(request , id , *args , **kwargs):
    ex = exercise.objects.get(id=id)
    return render(request,"exers_tea_temp.html",{'exercise' : ex})
# def lookup_view(request,id):
#     obj = exercise.objects.get(id = id)
#     return render(request,"lookup_temp.html",{'obj' : obj})
# def delete_view(request , id):
#     obj = get_object_or_404(exercise, id=id)
#     if request.method == "POST":
#         print("in deleting" , obj)
#         obj.delete()
#         print("deleted")
#     return render(request,"exer_delete_temp.html" , {'obj' : obj})