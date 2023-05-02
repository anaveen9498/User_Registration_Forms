from django.shortcuts import render
from app.models import *
from app.forms import *


from django.http import HttpResponse
# Create your views here.


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



            return HttpResponse('Register Your Details Successfully!!!')
        return HttpResponse('Your Inserted Data Is Invalid')
    return render(request,'registration.html',s)