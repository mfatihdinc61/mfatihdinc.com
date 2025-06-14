
# Register your models here.

from django.contrib import admin
from django.db import models

from .models import MarkdownProject, Thought
from tinymce.widgets import TinyMCE


@admin.register(MarkdownProject)
class MarkdownProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "created_at")


@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "created_at")
