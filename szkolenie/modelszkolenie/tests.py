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
    
    


# Create your tests here.
