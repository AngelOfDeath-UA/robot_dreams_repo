from django.test import TestCase
from user.models import User


class TestUserCreation(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(first_name='testcase', age=18)

    def test_creation_user(self):
        self.assertTrue(self.user is not None)

    def test_user(self):
        resp = self.client.get(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 200)

    def test_dell_user(self):
        resp = self.client.delete(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 204)


