from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.shortcuts import reverse


#Forms

    #register form
class TestRegisterForm(TestCase):

    def setUp(self):
        self.form_data = {'username': 'testusername',
                          'email': 'testemail@email.com',
                          'password1': 'test321123',
                          'password2': 'test321123'}

    def test_register_form_is_valid(self):
        form = UserRegisterForm(data=self.form_data)
        self.assertTrue(form.is_valid())


    def test_register_form_is_invalid(self):
        form = UserRegisterForm(data={'username':'testusername',
                                      'email': 'testemail@email.com',
                                      'password1': 'test321123',
                                      'password2': 'test321121'})
        self.assertFalse(form.is_valid())

    #user creation form
class TestUserUpdateForm(TestCase):

    def setUp(self):
        self.form_data = {'username': 'testusername', 'email': 'testemail@email.com'}

    def test_user_update_form_is_valid(self):
        form = UserUpdateForm(data=self.form_data)

        self.assertTrue(form.is_valid())

    def test_user_update_form_is_invalid(self):
        form = UserUpdateForm(data={'username': 'testusername', 'email': ''})

        self.assertFalse(form.is_valid())

    #profile update form
class TestProfileUpdateForm(TestCase):

    def setUp(self):
        self.form_data = {'image': 'default.png', 'about_myself': 'hi!'}

    def test_profile_update_form_is_valid(self):
        form = ProfileUpdateForm(data=self.form_data)

        self.assertTrue(form.is_valid())


#Views

    #Register
class SignUpTest(TestCase):

    def setUp(self):
        self.data = {
            'username': 'testuser',
            'email': 'email@memail.com',
            'password1': 'test321123',
            'password2': 'test321123'
        }

    def test_register(self):
        response = self.client.post('/register/', self.data, follow=True)
        self.assertTrue(response.context)

    def test_register_page(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'users/register.html')


    #Login
class LogInTest(TestCase):

    def setUp(self):
        self.data = {
            'username': 'testuser',
            'password': 'test321123'
        }

        User.objects.create_user(**self.data)

    def test_login(self):
        response = self.client.post('/login/', self.data, follow=True)
        self.assertTrue(response.context['user'].is_active)





