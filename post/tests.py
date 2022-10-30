from urllib import response
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from post.models import Post


class PostListTestCase(APITestCase):
    
    def setUp(self) -> None:
        user1 = User.objects.create_user(
            username='admin', email='kevinujunior@gmail.com', password='admin')
        user2 = User.objects.create_user(
            username='udit', password='udit')
        Post.objects.create(user=user1, title='First Post', description='Kek')
        Post.objects.create(user=user2, title='Second Post',
                            description='Sed lyf')
        
    def test_post_create_(self):
        self.client.login(username='udit', password='udit')
        data = {
             'title' : 'Bob kek' , 'description' : 'post desc'
        }
        response = self.client.post('/api/posts/', data)
        print("POST : '/api/posts/'")
        print("POSITIVE: Post created Successfully : ", "INPUT = ", data,"\n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_without_desc(self):
        self.client.login(username='udit', password='udit')
        data = {
             'description' : 'post desc'
        }
        response = self.client.post('/api/posts/', data)
        print("POST : '/api/posts/'")
        print("NEGATIVE: Post request Without Title: ", "INPUT = ", data,"\n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_delete(self):
        self.client.login(username='admin', password='admin')
        response = self.client.delete('/api/posts/1/')
        print("DELETE : '/api/posts/1'")
        print("POSITIVE: Post deleted Succefully: \n",)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_post_like(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/api/like/2')
        print("POST : '/api/like/2'")
        print("POSITIVE: Post liked Succefully: \n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_unlike(self):
        self.client.login(username='udit', password='udit')
        self.client.post('/api/like/1')
        response = self.client.post('/api/unlike/1')
        print("POST : '/api/unlike/1'")
        print("POSITIVE: Post unliked Succefully: \n",)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_comment(self):
        print("\n")
        self.client.login(username='udit', password='udit')
        data = {'comment': 'wae sar wae'}
        response = self.client.post('/api/comment/1', data)
        print("POST : '/api/comment/1'")
        print("POSITIVE: Comment Created Succefully: ", "INPUT = ", data,"\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_post_comment_empty(self):
        print("\n")
        self.client.login(username='udit', password='udit')
        data = {'comment': ''}
        response = self.client.post('/api/comment/1', data)
        print("POST : '/api/comment/1'")
        print("NEGATIVE: Comment Cant't be created: ", "INPUT = ", data,"\n")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_post_detail(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/api/posts/1/')
        print("GET : '/api/posts/1'")
        print("POSITIVE: Post detail View: ", "RESPONSE = " , response.json(),"\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list(self):
        self.client.login(username='udit', password='udit')
        response = self.client.get('/api/all_posts/')
        print("GET : '/api/all_posts/1'")
        print("POSITIVE: All posts by current user: ", "RESPONSE = " , response.json(),"\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
