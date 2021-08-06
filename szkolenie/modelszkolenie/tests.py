from django.test import TestCase
from modelszkolenie.models import User

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
        user1 = User.objects.create(imie="Michal", nazwisko="Bodura")
        user2 = User.objects.create(imie="Michal", nazwisko="Bodura")
        queryset = User.objects.filter(imie="Michal2")
        print(queryset)

    # False
    def test_ifUsersEquals_one(self):
        user1 = User.objects.create(imie="Michal", nazwisko="Bodura")
        user2 = User.objects.create(imie="Michal", nazwisko="Bodura")
        self.assertEquals(user1,user2)
     
    def test_ifUsersEquals_two(self):
        user1 = User.objects.create(id=6, imie="Michal", nazwisko="Bodura",email="michal_bodura@iutechnology.pl", nrDowodu="CDJ757557", jezyk="EN")
        user2 = User.objects.create(id=7, imie="Michal", nazwisko="Bodura",email="michal_bodura@iutechnology.pl", nrDowodu="CDJ757557", jezyk="EN")
        self.assertEquals(user1,user2)
    





# Create your tests here.
