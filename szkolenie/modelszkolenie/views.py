from .serializers import CompanySerializer, UserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Company, User
from rest_framework import generics

# Rest Framework ViewSets

# Create your views here.
def home(request):
    return render(request, 'modelszkolenie/home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'modelszkolenie/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'modelszkolenie/login.html', {'form': AuthenticationForm(), 'error':'Haslo i nazwa uzytkownika niezgodne'})
        else:
            login(request, user)
            return redirect('home')


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

