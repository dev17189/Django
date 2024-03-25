from django.shortcuts import render,redirect

# Create your views here.



def HomePage(request):
    return render (request,'home.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        return redirect('home')
    return render (request,'login.html')

def LogoutPage(request):
    return redirect('login')

def VotePage(request):
    return render (request,'vote.html')

def ResultPage(request):
    return render (request,'results.html')