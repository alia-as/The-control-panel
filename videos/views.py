from django.shortcuts import render , get_object_or_404
from .models import film
from .forms import film_form

# Create your views here.
def video_view(request,*args,**kwargs):
    all_movies = film.objects.all()
    return render(request,"film_temp.html",{'t' : all_movies})

def upload_view(request , *args,**kwargs):
    myform = film_form()
    if request.method == "POST":
        myform = film_form(request.POST)
        if myform.is_valid():
            print("CLeaned data :\t",myform.cleaned_data)
            myform.save()
        else:
            print("Errors: \t",myform.errors)
    return render(request , "upload_temp.html",{'form' : myform})
# def upload_view(request,*args,**kwargs):
#     if request.method == "POST" :
#         form = film_form(request.POST or None)
#         print("Heeree i s the formmmmmmmmmmmmmmmmmm")
#         if form.is_valid():
#             print("OKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk")
#             form.save()
#             form = film_form()
#         else:
#             print(form.errors)
#     else:
#         form = film_form()
#     contex = {'form' : form}
#     return render(request,"upload_temp.html",contex)