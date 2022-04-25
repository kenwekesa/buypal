
#from accounts.models import Userlogin
#from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required

from django.shortcuts import  render, redirect

from django.contrib import messages


from django.shortcuts import render

from accounts.models import Profile

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm

from django.contrib.auth.forms import AuthenticationForm #add this

from django.shortcuts import render, redirect

# Create your views here.







#@login_required
def home(request):
    #context = {'posts': Post.objects.all()}
    return render(request, 'buypal/index.html')#,context)

def news_view(request):
    #context = {'posts': Post.objects.all()}
    return render(request, 'buypal/news.html')#,context)

def login_view(request):
    #context = {'posts': Post.objects.all()}
  
    if request.method == "POST":
	    form = AuthenticationForm(request, data=request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)
		    if user is not None:
			    login(request, user)
			    return redirect("user-home")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="forms/login.html", context={"login_form":form})



def signup_view(request):
    #context = {'posts': Post.objects.all()}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')

            Profile.objects.create(user=user, full_name = full_name, email=email)

            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            

            messages.info(request, f"You are signed up successfully, login to proceed.")    
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'forms/signup.html', {'form': form})
    #return render(request, 'forms/signup.html')#,context)
    
@login_required
def userdashboard_view(request):
    return render(request, 'buypal/userdashboard.html')

@login_required
def edit_profile_view(request):
    #context = {'posts': Post.objects.all()}
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')

            Profile.objects.create(user=user, full_name = full_name, email=email)

            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            

            messages.info(request, f"You are signed up successfully, login to proceed.")    
            return redirect('login')
    else:
        form = SignUpForm(instance=request.user)
    return render(request, 'forms/signup.html', {'form': form})
    #return render(request, 'forms/signup.html')#,context)
