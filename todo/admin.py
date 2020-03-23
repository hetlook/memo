from django.contrib import admin

from .models import Todo
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created', 'updated', 'important', 'finish')
    list_editable = ['updated', 'important', 'finish']