from django.contrib import admin
from webapp.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'due_date', 'created_at', 'updated_at')
    list_filter = ['due_date']
    search_fields = ('description','detailed_description', 'status')
    fields = ('description','detailed_description', 'status', 'due_date', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


