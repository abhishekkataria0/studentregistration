from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    if request.method=='GET':   
        context ={}
        return render(request,'accounts/index.html',context)


def signup_view(request):
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            subject="thank you"
            message="welcome to student registration"
            from_email = settings.EMAIL_HOST_USER
            to_list=[user.email,settings.EMAIL_HOST_USER ]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            #login
            login(request,user)
            return redirect('student:home')
    else:
        form=RegistrationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method =='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('student:home')
    else:
        form =AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

@login_required(login_url="/accounts/login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('student:home'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
    




def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')



