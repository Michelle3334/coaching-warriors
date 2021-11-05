"""Course app view testcases"""
from django.test import TestCase


class TestCourseListViews(TestCase):
    """Test Course list view"""
    def test_course_list(self):
        """Test Coach list view"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
