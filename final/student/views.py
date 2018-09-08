from django.shortcuts import render,redirect

from django.http import HttpResponse
from . import forms
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student_form1,Student_form2,Student_form3,Student_form4
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.
@login_required(login_url="/accounts/login")
def first_page(request):

    if request.method == 'GET':
        try:
            status=request.user.student_form1.First_name
            if status!=None:
                return redirect('student:Second_page') 
        except ObjectDoesNotExist as e:
            form=forms.Stuform1()

    else:
        form=forms.Stuform1(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=request.user
            obj.save()
            return redirect('student:Second_page')
    context ={
        'stu_form1':form
    }
    return render(request,'first_page.html',context)

@login_required(login_url="/accounts/login")
def Second_page(request):
    if request.method == 'GET':
        try:
            status=request.user.student_form2.Mother_name
            if status!=None:
                if status=="Awaited":
                    return redirect('student:Fourth_page') 
                else:
                    return redirect('student:Third_page') 
        except ObjectDoesNotExist as e:
            form=forms.Stuform2() 
    else:
        form=forms.Stuform2(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=request.user
            obj.save()
            status=request.user.student_form2.Status_of_twefth_result
            if status=="Awaited":
                return redirect('student:Fourth_page') 
                 
            else:
                return redirect('student:Third_page') 
               
    context ={
        'stu_form2':form
    }
    return render(request,'Second_page.html',context)


def Third_page(request):
    if request.method == 'GET':
        try:
            status=request.user.student_form3.Subject1_marks
            if status!=None:
                return redirect('student:Fourth_page') 
        except ObjectDoesNotExist as e:
            form=forms.Stuform3()
    else:
        form=forms.Stuform3(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=request.user
            obj.save()
            return redirect('student:Fourth_page')
    context ={
        'stu_form3':form
    }
    return render(request,'Third_page.html',context)



@login_required(login_url="/accounts/login")
def Fourth_page(request):
    if request.method == 'GET':
        try:
            status=request.user.student_form4.candidate_photo
            if status!=None:
                status_1=request.user.student_form2.Status_of_twefth_result
                if status_1=="Awaited":
                    return redirect('student:Student_full_info') 
                else:
                    return redirect('student:Alt_student_full_info') 
        except ObjectDoesNotExist as e:
            form=forms.Stuform4()
    else:
        form=forms.Stuform4(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=request.user
            obj.save()
            status=request.user.student_form2.Status_of_twefth_result
            if status=="Awaited":
                return redirect('student:Student_full_info') 
            else:
                return redirect('student:Alt_student_full_info') 
            
    context ={
        'stu_form4':form
    }
    return render(request,'Fourth_page.html',context)





@login_required(login_url="/accounts/login")
def Student_full_info(request):

    args = {'user': request.user}
    return render(request, 'Student_full_info.html',args) 
    if request.method == 'GET':
        HttpResponse("thank you")

@login_required(login_url="/accounts/login")
def Alt_student_full_info(request):
    args = {'user': request.user}
    return render(request, 'Alt_student_full_info.html',args) 

        


def Prob_form(request):
    if request.method == 'GET':
        form=forms.Prob_form()
    else:
        form=forms.Prob_form(request.POST)

        if form.is_valid():
            obj = form.save()
            return HttpResponse("hello")
    context ={
        'Prob_form':form
    }
    return render(request,'Prob_form.html',context)
    
    


def Contact(request):
    if request.method =="GET":
        return render(request,'Contact.html')

def edit(request, user):
    user=request.user
    rest=get_object_or_404(models.student_form1 ,user)
    if request.method == 'GET':
        form=rest
    else:
        form=rest

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=request.user
            obj.save()
            return HttpResponse("hello")
    context ={
        'rest':form
    }
    return render(request,'first_page.html',context)







 