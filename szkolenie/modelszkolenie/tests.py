from django.test import TestCase, SimpleTestCase
from django.apps.registry import Apps
from django.db import models
from modelszkolenie.models import Company, User, Training
import datetime


class TestModelDefinition(SimpleTestCase):
    
    def test_model_definition(self):
        test_apps = Apps(['modelszkolenie'])

        class TestModel(models.Model):
            class Meta:
                apps = test_apps
        
        self.assertNull()

class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(imie="Michal", nazwisko="Bodura")
        User.objects.create(email="piotr.nowak@iutechnology.pl")
    
    # Sprawdzenie poprawnosci modelu pod wzgledem atrybutu - poprawna nazwa atrybutu
    def test_attributes(self):
        user1 = User.objects.get(imie="Michal")
        user2 = User.objects.get(email="piotr.nowak@iutechnology.pl")
        queryset = [user1, user2]
        self.assertTrue(queryset,"Cos nie poszlo z atrybutami")
    
    # Sprawdzanie nazwy atrybutu - bledna nazwa atrybutu
    def test_attributes2(self):
        user1 = User.objects.get(imie="Michal")
        user2 = User.objects.get(email="piotr.nowak@iutechnology.pl")
        queryset = [user1, user2]
        self.assertTrue(queryset,"Cos nie poszlo z atrybutami")

    def test_ifPiotrNowakExists(self):
        User.objects.create(imie="Piotr", nazwisko="Nowak")
        ex1 = User.objects.get(imie="Piotr", nazwisko="Nowak")
        self.assertTrue(ex1,"Nie ma Piotra Nowaka na liscie")

    def test_ifMichalIsInList(self):
        user1 = User.objects.create(imie="Michal", nazwisko="Bodura")
        user2 = User.objects.create(imie="Michal", nazwisko="Bodura")
        queryset = User.objects.filter(imie="Michal")
        self.assertTrue(queryset,"Nie ma uzytkownika o imieniu Michal na liscie")

    # False
    def test_ifUsersEquals_one(self):
        user1 = User.objects.create(imie="Michal", nazwisko="Bodura")
        user2 = User.objects.create(imie="Michal", nazwisko="Bodura")
        self.assertEquals(user1,user2,"Nie sa rowne")
     # True
    def test_ifUsersNotEquals(self):
        user1 = User.objects.create(imie="Michal", nazwisko="Bodura",email="michal_bodura@iutechnology.pl", nrDowodu="CDJ757557", jezyk="EN")
        user2 = User.objects.create(imie="Michal", nazwisko="Bodura",email="michal_bodura@iutechnology.pl", nrDowodu="CDJ757557", jezyk="EN")
        self.assertNotEquals(user1,user2,"Istnieje redundacja w bazie, prosze to zweryfikowac")

    # Sprawdzam typ zmiennej
    def test_type(self):
        User.objects.create(imie="Piotr", nazwisko="Nowak")
        ex1 = User.objects.get(imie="Piotr", nazwisko="Nowak")
        self.assertEqual(ex1.imie + " " + ex1.nazwisko, 'Piotr Nowak')
        

    
    

class CompanyTestCase(TestCase):

    def test_ifNotEquals(self):
        company1 = Company.objects.create(nazwa="IU Technology", adres="Dubois 114/116")
        company2 = Company.objects.create(nazwa="IU Technology", adres="Dubois 112")
        self.assertNotEquals(company1,company2)


class TrainingTestCase(TestCase):

    def test_ifTrainingStartsSeptember(self):
        d = datetime.date.today()
        training = Training.objects.create(nazwa="Testowe szkolenie", date=d)
        print(d)

# Create your tests here.
