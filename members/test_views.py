"""Members app view testcases"""
from django.test import TestCase
from django.contrib.auth.models import User


class TestMemberViews(TestCase):
    """Test Member app views"""
    def setUp(self):
        """Set up test user"""
        self.user = User.objects.create_user(
            username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_user_login(self):
        """Test user login view"""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_member_view_profile(self):
        """Test Member profile view"""
        self.client.login(username='test', password='12test12')
        response = self.client.get('/members/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_booking_view(self):
        """Test Bookings view"""
        self.client.login(username='test', password='12test12')
        response = self.client.get('/member_booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'member_booking.html')

    def test_create_booking_view(self):
        """Test Create Booking view"""
        self.client.login(username='test', password='12test12')
        response = self.client.get('/create_booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_booking.html')
