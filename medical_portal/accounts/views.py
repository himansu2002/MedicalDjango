from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import PatientProfile, DoctorProfile
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'patient':
            form = PatientSignUpForm(request.POST, request.FILES)
        else:
            form = DoctorSignUpForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PatientSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    if user.is_patient:
        profile = PatientProfile.objects.get(user=user)
    else:
        profile = DoctorProfile.objects.get(user=user)
    return render(request, 'accounts/profile.html', {'profile': profile})




def logout_view(request):
    logout(request)
    return redirect('login')  
