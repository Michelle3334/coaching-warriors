"""Contactemail app view testcases"""
from django.test import TestCase


class TestContactemailViews(TestCase):
    """Test Contactemail app view"""
    def test_contact(self):
        """Test contact form view"""
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
