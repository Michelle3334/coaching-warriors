"""Members model testing"""
from django.test import TestCase
from django.contrib.auth.models import User
from course.models import Course
from coaches.models import Coach
from .models import Booking


class TestModels(TestCase):
    """Testing member model"""
    def setUp(self):
        """Set up test user"""
        self.user = User.objects.create_user(
            username='angie', password='12test12')
        self.user.save()
        self.course = Course.objects.create(
            course_name='Test course',
            slug='test_course',
            status='1')
        self.course.save()
        self.coach = Coach.objects.create(
            coach_name='Test coach',
            email='test@gmail.com',
            title="Test Title",
            status='1')
        self.coach.save()

    def test_member_string_method_returns_coach(self):
        """Test string is returned"""
        self.client.login(username='angie', password='12test12')
        self.coach = 'Test coach'
        self.course = 'Test course'
        item = Booking.objects.create(
#            user='angie',
#            course='Test course',
#            coach='Test Coach',
            booking_date='2021-12-15')
        self.assertEqual(str(item), '2021-12-15')
