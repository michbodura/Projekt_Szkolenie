from django.test import TestCase
from django.contrib.auth.models import User

class AuthUserTestCase(TestCase):
    def test_ifSuperUser(self):
        superuser = User.objects.create_superuser(
            username='user',
            email='michal_bodura@iutechnology.pl',
            password='Monitor2020',
        )
        superuser.has_perm('auth.change_user')

