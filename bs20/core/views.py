from django.shortcuts import redirect, render
from .models import SignupTB

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        uname = request.POST.get('Username')
        em = request.POST.get('email')
        upass = request.POST.get('password')
        ucnfpass = request.POST.get('password')
        SignupTB(Username=uname,Email=em,Password=upass,CnfPassword=ucnfpass).save() 
        return redirect("Signin")  
    return render(request, 'signup.html', {"h1":"Welcome to this Page"})    

def signin(request):
    if request.method == "POST":
        un = request.POST.get('Username')
        upass = request.POST.get('Password')
        try:
            db1 = SignupTB.objects.get(Username=un,Password=upass)
        except SignupTB.DoesNotExist:
            return render(request, 'signup.html')
        else:
            request.session['uid']=db1.id
            return redirect('Home')
    return render(request, 'signin.html') 




