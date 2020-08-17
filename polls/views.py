from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserRegisterForm
from .models import register
from django.conf import settings
from django.contrib.auth import authenticate,get_user_model,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html')

def log(request):
    form1 = UserLoginForm(request.POST or None)
    if form1.is_valid():
        if request.POST:
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
        #context = {'form1': form1, }
                                            #login.......

    next = request.GET.get('next')
    form2 = UserRegisterForm(request.POST or None)
    if form2.is_valid():
        user = form2.save(commit=False)
        password1 = form2.cleaned_data.get('password1')
        user.set_password(password1)
        user.save()
        new_data=register(Username=request.POST['username'],Email=request.POST['email'],Password=request.POST['password1'],City=request.POST['city'])
        new_data.save()
        if next:
            return redirect(next)            
        return redirect('/')

    context = {
        'form2': form2,'form1':form1,
    }
    return render(request, "login.html", context)                                        
    