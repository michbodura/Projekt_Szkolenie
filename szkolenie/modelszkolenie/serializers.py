from rest_framework import serializers
from .models import Company, CompletedTraining,  User, Training

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','imie','nazwisko','email','nrDowodu','jezyk','firma']

class CompanySerializer(serializers.ModelSerializer):

    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ['id', 'nazwa','adres', 'users']

class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training
        fields = ['id', 'nazwa','czas','uczestnicy']

class CompletedTraningSerializer(serializers.ModelSerializer):
    expiration_date = serializers.SerializerMethodField()

    class Meta:
        model = CompletedTraining
        fields = ["osoba","szkolenie","data_ukonczenia","expiration_date"]

    def get_expiration_date(self, obj):
        return obj.expiration_date


    

    

