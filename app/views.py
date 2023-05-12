from django.shortcuts import render
from app.models import *
from app.forms import *

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required



from django.http import HttpResponse


from django.core.mail import send_mail
# Create your views here.


def home(request):


    if request.session.get('username'):
        username=request.session.get('username')
        D={'username':username}
        return render(request,'home.html',D)

    return render(request,'home.html')





def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    s={'UFO':UFO,'PFO':PFO}


    if request.method=='POST' and request.FILES:
        Object_Of_User=UserForm(request.POST)
        Object_Of_Profile=ProfileForm(request.POST,request.FILES)
        if Object_Of_User.is_valid() and Object_Of_Profile.is_valid():
            Not_Saved_User_Data=Object_Of_User.save(commit=False)


            #password=UFO.cleaned_data['password']
            #Not_Saved_User_Data.set_password(password)



            Not_Saved_User_Data.set_password(Object_Of_User.cleaned_data['password'])
            Not_Saved_User_Data.save()


            Not_Saved_Profile_Data=Object_Of_Profile.save(commit=False)
            Not_Saved_Profile_Data.username=Not_Saved_User_Data
            Not_Saved_Profile_Data.save()

            send_mail('Enter Your Acount Details',
                      'your acount is successfully created....thank you for register your details',
                      'naveenavula130@gmail.com',
                      [Not_Saved_User_Data.email],
                      fail_silently=True)
                      

            return HttpResponse('Register Your Details Successfully!!!')
        return HttpResponse('Your Inserted Data Is Invalid')
    return render(request,'registration.html',s)






def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid User Name or Password')
    return render(request,'user_login.html')




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))