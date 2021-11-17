"""Course app view testcases"""
from django.test import TestCase


class TestCourseListViews(TestCase):
    """Test Course list view"""
    def test_course_list(self):
        """Test Coach list view"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestGalleryViews(TestCase):
    """Test Gallery view"""
    def test_gallery(self):
        """Test Gallery view"""
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')


class TestAboutViews(TestCase):
    """Test About view"""
    def test_about(self):
        """Test About view"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
