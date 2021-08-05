from .serializers import CompanySerializer, UserSerializer, TrainingSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Company, User, Training
from rest_framework import generics, permissions
from rest_framework.response import Response
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


class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class TrainingList(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = TrainingSerializer(queryset, many=True)
        return Response(serializer.data)