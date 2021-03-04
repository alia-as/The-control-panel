from django.shortcuts import render
from .models import film
from django.core.files.storage import FileSystemStorage

# Create your views here.
def video_view(request,*args,**kwargs):
    all_movies = film.objects.all()
    return render(request,"film_temp.html",{'t' : all_movies})

def upload_view(request , *args,**kwargs):
    movie = film()
    context = {}
    if request.method == "POST":
        video = request.FILES["video"]
        fs = FileSystemStorage()
        name = fs.save(video.name , video)
        context['url'] = fs.url(name)
        movie.movie_url = fs.url(name)
        movie.movie_name = video.name
        print(movie.movie_name)
        movie.save()
    return render(request , "upload_temp.html",context)