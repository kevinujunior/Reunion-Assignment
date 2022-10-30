from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from user.serializers import UserSerializer
from post.serializers import PostSerializer

    
class FollowTestView(APITestCase):
    def test_follow_test(self):
        self.user = User.objects.create_user(
            username='admin', email = 'kevinujunior@gmail.com', password='admin')
        User.objects.create_user(
            username='udit', password='udit')
        login = self.client.login(username='admin', password='admin')
        response = self.client.post('/api/follow/2')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
