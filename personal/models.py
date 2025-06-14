# Create your models here.

from django.db import models
from django.urls import reverse
import re, markdown



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})




class MarkdownProject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(help_text="Short summary for list page", blank=True)
    markdown_file = models.FileField(upload_to='markdown_files/')
    github_url = models.URLField(blank=True, null=True)
    # tech_stack = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # @property
    # def tech_tags(self):
    #     return [tag.strip() for tag in self.tech_stack.split(',')] if self.tech_stack else []

    tech_stack = models.CharField(
        max_length=255,
        help_text="Comma-separated list of technologies (e.g. Python, Django, Bootstrap)",
        blank=True
    )



class Thought(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(help_text="Short summary of your thought (for listing)")
    markdown_file = models.FileField(upload_to='thoughts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def html_content(self):

        if not self.markdown_file:
            return ""

        with self.markdown_file.open('rb') as f:
            raw_md = f.read().decode('utf-8')

        # Convert Obsidian-style images to Markdown image syntax
        md = re.sub(r'!\[\[(.*?)\]\]', r'![Image](/media/thoughts/\1)', raw_md)

        return markdown.markdown(md)

