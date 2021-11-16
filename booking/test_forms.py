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

    def test_last_name_is_required(self):
        """Test if last name required"""
        form = BookingForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('course', form.errors.keys())
        self.assertEqual(form.errors[
            'last_name'][0], 'This field is required.')

    def test_email_address_is_required(self):
        """Test if email address required"""
        form = BookingForm({'email_address': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email_address', form.errors.keys())
        self.assertEqual(form.errors[
            'email_address'][0], 'This field is required.')

    def test_telephone_is_required(self):
        """Test if telephone required"""
        form = BookingForm({'telephone': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('telephone', form.errors.keys())
        self.assertEqual(form.errors[
            'telephone'][0], 'This field is required.')

    def test_coach_is_required(self):
        """Test if coach required"""
        form = BookingForm({'coach': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('coach', form.errors.keys())
        self.assertEqual(form.errors[
            'coach'][0], 'This field is required.')

    def test_course_is_required(self):
        """Test if course required"""
        form = BookingForm({'course': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('course', form.errors.keys())
        self.assertEqual(form.errors[
            'course'][0], 'This field is required.')

    def test_date_is_required(self):
        """Test if date required"""
        form = BookingForm({'requested_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('requested_date', form.errors.keys())
        self.assertEqual(form.errors[
            'requested_date'][0], 'This field is required.')
