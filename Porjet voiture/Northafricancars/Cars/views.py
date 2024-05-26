from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm

# Create your views here.
def acceuil(request):
    return render(request,'acceuil.html')

def service(request):
    return render(request,'service.html')

def aboutus(request):
    return render(request,'about-us.html')


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Rediriger vers la page d'accueil après inscription
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('acceuil')  # Rediriger vers la page d'accueil après connexion
    else:
        form= LoginForm()
        return render(request,'Cars/login.html',{'from':form})
