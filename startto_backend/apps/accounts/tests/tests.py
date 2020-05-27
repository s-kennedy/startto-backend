# Django
from django.contrib.auth.models import User

# App
from startto_backend.apps.accounts.models import Profile

# Rest Framework
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

PASSWORD = 'Pass1234'

# Create your tests here.
class RegistrationTestCase(APITestCase):
    def setUp(self):
        self.user_endpoint = reverse('account-api:user-list')

    def test_user_endpoint_exists(self):
        self.assertEqual(self.user_endpoint, '/api/v1/users/')

    def test_get_users_with_good_data(self):
        response = self.client.get(self.user_endpoint, format='json')

        self.assertEqual(response.data, [])

    def test_post_user_with_good_data(self):
        data = {
            'email': 'test@test.com',
            'password': PASSWORD,
            'first_name': 'FirstName',
            'last_name': 'LastName',
        }
        response = self.client.post(self.user_endpoint, data=data, format='json')

        self.assertEqual(response.data.get('id'), 1)
        self.assertEqual(response.data.get('email'), data['email'])

        user = User.objects.first()
        self.assertEqual(response.data.get('id'), user.id)
        self.assertEqual(response.data.get('email'), user.email)

        self.assertEqual(data['first_name'], user.first_name)
        self.assertEqual(data['last_name'], user.last_name)

        profile = Profile.objects.first()
        self.assertEqual(profile.user.email, response.data.get('email'))

