"""Course model testing"""
from django.test import TestCase
from .models import Course


class TestModels(TestCase):
    """Testing course model"""
    def test_course_string_method_returns_course(self):
        """Test string is returned"""
        item = Course.objects.create(
            course_name='Test course',
            slug='test_course',
            status='1')
        self.assertEqual(str(item), 'Test course')
