from urllib import response
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from user.serializers import UserSerializer
from post.serializers import PostSerializer


class UserTestView(APITestCase):
    print("\n")
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='admin', email='kevinujunior@gmail.com', password='admin')
        User.objects.create_user(
            username='udit', password='udit')
        User.objects.create_user(username='kek', password='kek')
        self.client.login(username='admin', password='admin')

    def test_follow(self):
        response = self.client.post('/api/follow/2')
        print("POSITIVE: User followed Successfully: \n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unfollow(self):
        self.client.post('/api/follow/3')
        response = self.client.post('/api/unfollow/3')
        print("POST : '/api/follow/3'")
        print("POSITIVE: User unfollowed Successfully: \n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unfollow_user_does_not_exist(self):
        self.client.post('/api/follow/2')
        response = self.client.post('/api/unfollow/4')
        print("POST : '/api/follow/4'")
        print("NEGATIVE: User does not exist: \n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_user(self):
        response = self.client.get('/api/user/')
        print("POSITIVE: User Details: \n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
