from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

# This function will add new item and show all item
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
           nm=fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           pw=fm.cleaned_data['password']
           reg=User(name=nm, email=em, password=pw)  # it save the data in db
           reg.save()
           fm=StudentRegistration()   # by using this form will cleaned after save
    else:
        fm=StudentRegistration()
    stud=User.objects.all()    # it show the all data on frontend
    return render(request,'add&show.html',{'form':fm, 'stu':stud})

# this function will update/edit
def update(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        
    return render(request,'update.html',{'form':fm})

# This function will delete records
def delete(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)        #pk=primary key
        pi.delete()
        return redirect('/')
        