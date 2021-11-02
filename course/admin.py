"""Display model in Django Admin panel"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Course


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    """Course Fields for display and filter"""
    prepopulated_fields = {'slug': ('course_name',)}
    list_display = ('course_name', 'slug', 'status', 'created_on')
    search_fields = ['course_name', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
