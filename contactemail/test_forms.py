"""Contactemail app forms testcases"""
from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """Tests for contact form"""
    def test_name_is_required(self):
        """Test if name required"""
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors[
            'name'][0], 'This field is required.')

    def test_email_address_is_required(self):
        """Test if email address is required"""
        form = ContactForm({'email_address': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email_address', form.errors.keys())
        self.assertEqual(form.errors[
            'email_address'][0], 'This field is required.')

    def test_message_is_required(self):
        """Test if message is required"""
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors[
            'message'][0], 'This field is required.')
