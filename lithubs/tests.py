from django.test import TestCase
from .models import User

# Create your tests here.

class CreateUserTestCase(TestCase):
    def setUp(self):
        self.user_model = User
    
    def test_create_user(self):
        user = self.user_model.objects.create_user(
            name = 'joe',
            username = 'joeblow',
            email = 'joe@gmail.com',
            bio = 'just joe',
            password = '123456'
        )
        
        self.assertEqual(user.name, 'joe')
        self.assertEqual(user.username, 'joeblow')
        self.assertEqual(user.email, 'joe@gmail.com')
        self.assertEqual(user.bio, 'just joe')
        

        

