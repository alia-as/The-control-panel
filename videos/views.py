from django.shortcuts import render , HttpResponse
from .models import film
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import FormView
# Create your views here.

allowed_suffix = [".mkv", '.mp4' , '.avi' , '.m4v']
def video_view(request,*args,**kwargs):
    all_movies = film.objects.all()
    return render(request,"film_temp.html",{'t' : all_movies})
def upload_view(request , *args,**kwargs):
    movie = film()
    context = {}
    if request.method == "POST":
        video = request.FILES["file"]
        if not check_suffix(video.name):
            resp = "<h1>Your file suffix isn't valid</h1> <p>It must be one of these suffix "
            suffs = ""
            for suffix in allowed_suffix: suffs = suffs + " <br> " + suffix[1:]
            return HttpResponse(resp + suffs + "</p>")
        fs = FileSystemStorage()
        name = fs.save(video.name , video)
        context['url'] = fs.url(name)
        movie.movie_url = fs.url(name)
        movie.movie_name = video.name
        print(movie.movie_name)
        movie.save()
    return render(request , "upload_temp.html",context)
def check_suffix(name):
    flag = False
    for suffix in allowed_suffix:
        if suffix in name:
            flag = True
    return flag