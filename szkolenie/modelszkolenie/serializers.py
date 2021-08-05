from rest_framework import serializers
from .models import Company, Training, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','imie','nazwisko','email','nrDowodu','jezyk']

    
class CompanySerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ['id', 'nazwa','adres', 'users']

class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training
        fields = ['id','poczatek','koniec','listCustomers']





