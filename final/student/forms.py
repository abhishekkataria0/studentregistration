from django import forms
from . import models

class Stuform1(forms.ModelForm):
    class Meta:
        model = models.Student_form1
        fields ='__all__'
        exclude =['user',]
    

class Stuform2(forms.ModelForm):
    class Meta:
        model = models.Student_form2
        fields ='__all__'
        exclude =['user',]

class Stuform3(forms.ModelForm):
    class Meta:
        model = models.Student_form3
        fields ='__all__'
        exclude =['user',]

class Stuform4(forms.ModelForm):
    class Meta:
        model = models.Student_form4
        fields ='__all__'
        exclude =['user',]

class Prob_form(forms.ModelForm):
    class Meta:
        model = models.Prob_form
        fields ='__all__'







        




