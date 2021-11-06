"""Course app view testcases"""
from django.test import TestCase
from .models import Course


class TestCourseListViews(TestCase):
    """Test Course list view"""
    def test_course_list(self):
        """Test Coach list view"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestCourseDetailViews(TestCase):
    """Test Course detail view"""
    def test_course_detail(self):
        """Test Course detail view"""
        item = Course.objects.create(
            course_name='Test course', slug='test_course', status='1')
        response = self.client.get(f'/slug:slug/{item.slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_detail.html')


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
