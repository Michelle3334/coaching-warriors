"""Booking app forms testcases"""
from django.test import TestCase
from .forms import BookingForm


class TestBookingForm(TestCase):
    """Tests for booking form"""
    def test_first_name_is_required(self):
        """Test if first name required"""
        form = BookingForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors[
            'first_name'][0], 'This field is required.')

    def test_additional_information_field_is_not_required(self):
        """Test additional information field is not required"""
        form = BookingForm({
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email_address': 'jdoe@gmail.com',
            'telephone': '0112223333',
            'course': 'Course1',
            'coach': 'Coach2',
            'date': '12/10/2021'})
        self.assertTrue(form.is_valid())
