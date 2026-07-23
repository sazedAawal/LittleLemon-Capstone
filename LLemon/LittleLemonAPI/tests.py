from django.test import TestCase
from .models import LLAPIMenuItem

# Create your tests here.
class TestMenuItemTest(TestCase):
    def test_get_item(self):
        item = LLAPIMenuItem.objects.create(
            title='IceCream',
            price = 80,
            inventory = 100,
        )
        self.assertEqual(str(item), 'IceCream : 80')

class MenuViewTest(TestCase):
    def setup(self):
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
