from django.test import TestCase
from .models import Contact
# Create your tests here.

class ContactTest(TestCase):
    def test_num(self):
        a=len(Contact.objects.all())
        Contact(name="tal").save()
        b=len(Contact.objects.all())
        self.assertEqual(b, a+1)
