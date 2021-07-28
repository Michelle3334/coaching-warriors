from django.contrib import admin
from .models import Course, Module, Lesson
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('course_name',)}
    list_display = ('course_name', 'slug', 'status', 'created_on')
    search_fields = ['course_name', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Module)
class ModuleAdmin(SummernoteModelAdmin):
    list_display = ('module_name', 'created_on')
    search_fields = ['module_name', 'content']
    summernote_fields = ('content')


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    list_display = ('lesson_name', 'created_on')
    search_fields = ['lesson_name', 'content']
    summernote_fields = ('content')
