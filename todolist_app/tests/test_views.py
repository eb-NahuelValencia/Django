from django.test import TestCase
import unittest
from todolist_app.views import CreateView, TaskList
from django.urls import reverse
import json
from datetime import datetime
from django.test import Client;
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from todolist_app.models import Task, Priority
from social_django.models import UserSocialAuth


class TaskCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        # self.user = User.objects.create(username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True) 
        # self.user.save()
        self.user = User.objects.create_user(username='testuser', password='12345')
        UserSocialAuth.objects.create(
            user=self.user,
            provider='eventbrite',
            uid='34563456',
            extra_data={
                'auth_time': 1567447106,
                'access_token': 'KLHJLJHLKJH',
                'token_type': 'bearer',
            }
        )

    def test_task_create(self):
        priority = Priority.objects.create(name="Normal")
        url = "/events/{}/task/create/".format("12345")
        task = Task.objects.create(name="Tarea1", created=datetime.now(), changed=datetime.now(), priority=priority, author=self.user, done=False, id_event=12345)
        # data =  {'name': 'task', 'priority':priority, 'created':date, 'changed': date, 'user':self.user}                     
        data = {'name': 'task', 'priority': priority}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class EventListViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(username='testuser1', password='123456')
        UserSocialAuth.objects.create(
            user=self.user,
            provider='eventbrite',
            uid='34563456',
            extra_data={
                'auth_time': 1567447106,
                'access_token': 'KLHJLJHLKJH',
                'token_type': 'bearer',
            }
        )

    def mocked_requests_get(*args, **_):
        class MockResponse:
            def __init__(self, json_data=None, status_code=200):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                with open('todolist_app/response_example.json', 'r') as f:
                    return json.loads(f.read())

            def raise_for_status(self):
                pass

        return MockResponse()

    # @unittest.mock.patch('requests.get', side_effect=mocked_requests_get)
    # def test_get_events(self, mocked_requests):
    #     login = self.client.force_login(UserSocialAuth.user)
    #     response = self.client.get('events/')
    #     self.assertEqual(response.status_code, 200)