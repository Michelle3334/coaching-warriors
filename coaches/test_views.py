"""Coaches app view testcases"""
from django.test import TestCase


class TestCoachListViews(TestCase):
    """Test Coach list view"""
    def test_coach_list(self):
        """Test Coach list view"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
