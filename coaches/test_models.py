"""Coach model testing"""
from django.test import TestCase
from .models import Coach


class TestModels(TestCase):
    """Testing coach model"""
    def test_coach_string_method_returns_coach(self):
        """Test string is returned"""
        item = Coach.objects.create(
            coach_name='Test coach',
            email='test@gmail.com',
            title="Test Title",
            status='1')
        self.assertEqual(str(item), 'Test coach')
