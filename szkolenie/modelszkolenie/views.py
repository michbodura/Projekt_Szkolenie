from .serializers import CompanySerializer, CompletedTraningSerializer, UserSerializer, TrainingSerializer
from django.shortcuts import render
from .models import Company, CompletedTraining,  User, Training
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

class TrainingList(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class TrainingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class TrainingUserList(generics.ListAPIView):
    serializer_class = CompletedTraningSerializer

    def get_queryset(self):
        uczestnik = User.objects.get(pk=self.kwargs['pk'])
        return CompletedTraining.objects.filter(osoba=uczestnik)

    
