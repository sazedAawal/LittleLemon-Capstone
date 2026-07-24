from django.test import TestCase
from .models import LLAPIMenuItem
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class TestMenuItemTest(TestCase):
    def test_get_item(self):
        item = LLAPIMenuItem.objects.create(
            title='IceCream',
            price = 80,
            inventory = 100,
        )
        self.assertEqual(str(item), 'IceCream : 80.00')

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = LLAPIMenuItem.objects.create(
            title='IceCream', price=80, inventory=100,
        )
        self.item2 = LLAPIMenuItem.objects.create(
                    title='Pizza', price=120, inventory=50,
                )
    def test_get_all(self):
        items = LLAPIMenuItem.objects.all()
        self.assertEqual(items.count(),2)
        self.assertIn(self.item1, items)
        self.assertIn(self.item2, items)

class RegistrationTest(APITestCase):
    def test_register_user(self):
        url = reverse('registration')
        data = {
            'username':'testuser',
            'email':'test@email.com',
            'password':'testPass123!',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())