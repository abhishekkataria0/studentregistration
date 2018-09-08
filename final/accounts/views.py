from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm
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
            #login
            login(request,user)
            return redirect('student:first_page')
    else:
        form=RegistrationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method =='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('student:first_page')
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
            return redirect(reverse('student:first_page'))
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



