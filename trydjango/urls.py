"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

from pages.views import home_view , student_view , teacher_view
from teacher.views import teacherview
from student.views import add_student
from videos.views import video_view , upload_view
from exercises.views import tea_add_exer_view , tea_exercises,stu_exercises , exercise_tea_view , exercise_stu_view, stu_upload_view # , lookup_view , delete_view
urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('', home_view),
    path('add-student/',add_student),
    path('upload/',upload_view),
    path('videos/',video_view),
    path('student/', student_view),
    path('teacher/', teacherview),
    path('admin/', admin.site.urls),
    path('add-exercise/',tea_add_exer_view),
    path('teacher-exercises/',tea_exercises),
    path('student-exercises/',stu_exercises),
    path('teacher-exercise/<int:id>/',exercise_tea_view),
    path('student-exercise/<int:id>/',exercise_stu_view),
    path('student-exercise/<int:id>/upload/',stu_upload_view),
    # path('student-exercise/<int:id>/',lookup_view,name = "exercise"),
    # path('student-exercise/<int:id>/delete/',delete_view,name = "delete_exercise"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)