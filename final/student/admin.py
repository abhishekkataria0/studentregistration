from django.contrib import admin
from . import models
from .models import Student_form1,Student_form2,Student_form3,Student_form4,Prob_form

# Register your models here.
admin.site.register(Student_form1)
admin.site.register(Student_form2)
admin.site.register(Student_form3)
admin.site.register(Student_form4)
admin.site.register(Prob_form)


