from .serializers import CompanySerializer, UserSerializer
from django.shortcuts import render
from .models import Company, User
from rest_framework import generics

# Rest Framework ViewSets

# Create your views here.
def home(request):
    return render(request, 'modelszkolenie/home.html')

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
