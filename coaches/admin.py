from django.contrib import admin
from .models import Coach
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Coach)
class CoachAdmin(SummernoteModelAdmin):

    search_fields = ['coach_name', 'content']
    list_display = ('coach_name', 'status')
    summernote_fields = ('about')
