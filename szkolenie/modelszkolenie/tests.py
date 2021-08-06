from django.test import TestCase
from modelszkolenie.models import Company, User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(imie="Michal", nazwisko="Bodura")
        User.objects.create(email="piotr.nowak@iutechnology.pl")
    
    # Sprawdzenie poprawnosci modelu pod wzgledem atrybutu - poprawna nazwa atrybutu
    def test_attributes(self):
        user1 = User.objects.get(imie="Michal")
        user2 = User.objects.get(email="piotr.nowak@iutechnology.pl")
    
    # Sprawdzanie nazwy atrybutu - bledna nazwa atrybutu
    def test_attributes2(self):
        user1 = User.objects.get(imie2="Michal")
        user2 = User.objects.get(email2="piotr.nowak@iutechnology.pl")
    
    def test_ifPiotrNowakExists(self):
        User.objects.create(imie="Piotr", nazwisko="Nowak")
        ex1 = User.objects.get(imie="Piotr", nazwisko="Nowak")

    def test_ifMichalInTraining(self):
        self.UserTestCase.setUp()
        queryset = User.objects.filter(imie="Michal")

    # False
    def test_ifUsersEquals_one(self):
        user1 = User.objects.create(imie="Michal", nazwisko="Bodura")
        user2 = User.objects.create(imie="Michal", nazwisko="Bodura")
        self.assertEquals(user1,user2)
     # True
    def test_ifUsersNotEquals(self):
        user1 = User.objects.create(imie="Michal", nazwisko="Bodura",email="michal_bodura@iutechnology.pl", nrDowodu="CDJ757557", jezyk="EN")
        user2 = User.objects.create(imie="Michal", nazwisko="Bodura",email="michal_bodura@iutechnology.pl", nrDowodu="CDJ757557", jezyk="EN")
        self.assertNotEquals(user1,user2)

class CompanyTestCase(TestCase):
    def test_ifNotEquals(self):
        company1 = Company.objects.create(nazwa="IU Technology", adres="Dubois 114/116")
        company2 = Company.objects.create(nazwa="IU Technology", adres="Dubois 112")
        self.assertNotEquals(company1,company2)
    





# Create your tests here.
