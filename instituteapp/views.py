from django.shortcuts import render,redirect
from .models import Courses
from .models import contactData,FeedbackData,RegistrationData
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
import datetime as dt
data1=dt.datetime.now()

#@login_required(login_url='login')
def homePage(request):
    return render(request,'homePage.html')

#@login_required(login_url='login')
def contactPage(request):
    if request.method=='GET':
        data= contactData.objects.all()
        return render(request,'contactPage.html')
    else:
         contactData(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            location= request.POST['location']
                ).save()
    return redirect(contactPage)

def servicePage(request):
    courses=Courses.objects.all()
    return render(request,'servicePage.html', {'courses':courses})

def feedbackPage(request):
    if request.method=='GET':
        feedbacks=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'feedbacks':feedbacks})
    else:
        FeedbackData(
        content=request.POST['feedback'],
        date=data1
        ).save()
        feedbacks=FeedbackData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'feedbacks':feedbacks})


def galleryPage(request):
    return render(request,'galleryPage.html')

def reg_Page(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST,request.FILES)
        if rform.is_valid():
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            city=request.POST.get('city')
            data=RegistrationData(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
                mobile=mobile,
                city=city
            )
            data.save()
            lform=LoginForm()
            return render(request,'loginPage.html',{'lform':lform})

        else:
            return HttpResponse("User Invalid Data")
    else:
        rform=RegistrationForm()
        return render(request,'registerPage.html',{'rform':rform})


def login_Page(request):
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=user,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')


        else:
             return HttpResponse("Login Failed")
    else:
        lform=LoginForm()
        return render(request, 'loginPage.html', {'lform':lform})
