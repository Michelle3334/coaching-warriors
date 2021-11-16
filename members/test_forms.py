"""Members app forms testcases"""
from django.test import TestCase
from .forms import UserRegisterForm, UserLoginForm, ProfileForm, CreateBookingForm


class TestUserRegisterForm(TestCase):
    """Test for user register form"""
    def test_username_is_required(self):
        """Test if user name required"""
        form = UserRegisterForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors[
            'username'][0], 'This field is required.')

    def test_password1_is_required(self):
        """Test if password1 required"""
        form = UserRegisterForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(form.errors[
            'password1'][0], 'This field is required.')

    def test_password2_is_required(self):
        """Test if password2 required"""
        form = UserRegisterForm({'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors[
            'password2'][0], 'This field is required.')

    def test_passwords_match(self):
        """Test if password1 and password2 match"""
        form = UserRegisterForm({
            'password1': 'testcoachs',
            'password2': 'coachtest'})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors[
            'password2'][0], 'You must type the same password each time.')


class TestUserLoginForm(TestCase):
    """Tests for user login form"""
    def test_username_is_required(self):
        """Test if login name required"""
        form = UserLoginForm({'login': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('login', form.errors.keys())
        self.assertEqual(form.errors[
            'login'][0], 'This field is required.')

    def test_password_is_required(self):
        """Test if password required"""
        form = UserLoginForm({'password': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors.keys())
        self.assertEqual(form.errors[
            'password'][0], 'This field is required.')


class TestProfileForm(TestCase):
    """Tests for update profile form"""
    def test_username_is_required(self):
        """Test if login name required"""
        form = ProfileForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors[
            'username'][0], 'This field is required.')

    def test_first_name_is_required(self):
        """Test if login name required"""
        form = ProfileForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors[
            'first_name'][0], 'This field is required.')

    def test_last_name_is_required(self):
        """Test if last name required"""
        form = ProfileForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors[
            'last_name'][0], 'This field is required.')

    def test_email_is_required(self):
        """Test if email required"""
        form = ProfileForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors[
            'email'][0], 'This field is required.')


class TestCreateBookingForm(TestCase):
    """Tests for create booking form"""
    def test_booking_date_is_required(self):
        """Test if booking date required"""
        form = CreateBookingForm({'booking_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('booking_date', form.errors.keys())
        self.assertEqual(form.errors[
            'booking_date'][0], 'This field is required.')

    def test_course_name_is_required(self):
        """Test if course name required"""
        form = CreateBookingForm({'course_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('course_name', form.errors.keys())
        self.assertEqual(form.errors[
            'course_name'][0], 'This field is required.')

    def test_coach_name_is_required(self):
        """Test if coach name required"""
        form = CreateBookingForm({'coach_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('coach_name', form.errors.keys())
        self.assertEqual(form.errors[
            'coach_name'][0], 'This field is required.')
