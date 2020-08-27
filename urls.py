from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('addstudent',views.addstudent),
    path('showstudent',views.showstudent),
    path('allstudent',views.allstudent),
    path('retrieve',views.retrieve),
    path('showstudentdetails',views.showstudentdetails),
    path('allstudentdetail',views.allstudentdetail),
]