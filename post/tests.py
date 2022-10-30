from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status



class PostListTestCase(APITestCase):

    def test_post_list(self):
        self.user = User.objects.create_user(
            username='admin', email = 'kevinujunior@gmail.com', password='admin')
        login = self.client.login(username='admin', password='admin')
        response = self.client.get('/api/all_posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    