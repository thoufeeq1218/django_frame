
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout



def home(request):

    return render(request,'app/index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')
        else:
            user = authenticate(username=username, password=pass1)
            if user is None:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname

                myuser.save()
                messages.success(request,"Acc created successfully")
                return redirect('loginn')
            else:
                messages.success(request, "User Already Exists")
                return redirect('logup')


    return render(request,'app/logup.html')


def loginn(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            # return render(request, "app/mypage.html", {"fname": fname})
            return redirect('mypage')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('loginn')

    return render(request, "app/login.html")


def logoutt(request):

    logout(request)
    # messages.success(request, "Logged Out Successfully!!")
    return render(request,"app/logout.html")

@login_required(login_url="loginn")
def mypage(request):

     return  render(request,'app/employe.html')


def contact(request):
    if request:
        return HttpResponse('<h1>Page was found</h1>')

@login_required(login_url="loginn")
def about(request):
    if request:
        return HttpResponse('<h1>Page was found</h1>')








        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


