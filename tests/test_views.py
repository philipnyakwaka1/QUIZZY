from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from quizes.models import Quiz
from results.models import Result

class SimpleTests(TestCase):

    def setUp(self):
        """
        Set up the test case by creating a client and a test user.

        This method is called before each test case is executed. It creates a client object using the Django test client and creates a test user with the username 'testuser' and password 'password'.

        Parameters:
            self (SimpleTests): The current test case instance.

        Returns:
            None
        """
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home-view'))
        self.assertEqual(response.status_code, 200)

    def test_profile_page_status_code(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('profile-view'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_code(self):
        response = self.client.get(reverse('login-view'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get(reverse('register-view'))
        self.assertEqual(response.status_code, 200)

    def test_logout_page_status_code(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('logout-view'))
        self.assertEqual(response.status_code, 200)


    def test_submit_page_get_request(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('submit-view'))
        self.assertEqual(response.status_code, 200)

    def test_search_page_status_code(self):
        response = self.client.get(reverse('search-view'))
        self.assertEqual(response.status_code, 200)

    def test_questions_page_status_code(self):
        response = self.client.get(reverse('questions-view'))
        self.assertEqual(response.status_code, 200)


    def test_register_user(self):
        response = self.client.post(reverse('register-view'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password',
            'confirm_password': 'password',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_user(self):
        response = self.client.post(reverse('login-view'), {
            'username': 'testuser',
            'password': 'password',
        })
        self.assertEqual(response.status_code, 302)

    def test_logout_user(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('logout-view'))
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.post(reverse('login-view'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')

    def test_invalid_register_user(self):
        response = self.client.post(reverse('register-view'), {
            'username': 'testuser', 
            'email': 'testuser@example.com',
            'password': 'password',
            'confirm_password': 'password',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username already exists.')


    def test_profile_page_context(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('profile-view'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.context)
        self.assertIn('courses', response.context)
        self.assertIn('today', response.context)
