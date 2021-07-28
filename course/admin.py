from django.contrib import admin
from .models import Course
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('course_name',)}
    list_display = ('course_name', 'slug', 'status', 'created_on')
    search_fields = ['course_name', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
