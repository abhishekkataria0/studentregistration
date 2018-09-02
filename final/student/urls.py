from django.conf.urls import url
from . import views
from django.urls import path

app_name='student'

urlpatterns=[
    path('first_page/',views.first_page,name="first_page"),
    path('Second_page/',views.Second_page,name="Second_page"),
    path('Third_page/',views.Third_page,name="Third_page"),
    path('Fourth_page/',views.Fourth_page,name="Fourth_page"),
    path('Student_full_info/',views.Student_full_info,name="Student_full_info"),
    path('Alt_student_full_info/',views.Alt_student_full_info,name="Alt_student_full_info"),
    path('Prob_form/',views.Prob_form,name="Prob_form"),
    path('Contact/',views.Contact,name="Contact"),

]