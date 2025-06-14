from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator

from .models import MarkdownProject, Thought
import markdown
import os
import re


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project_list(request):
    projects = MarkdownProject.objects.all()

    for p in projects:
        if p.tech_stack:
            p.tech_tags = [tag.strip() for tag in p.tech_stack.split(',')]
        else:
            p.tech_tags = []

    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(MarkdownProject, slug=slug)

    if not project.markdown_file:
        return HttpResponse("No file uploaded", status=404)

    # Open in binary mode, then decode
    with project.markdown_file.open(mode='rb') as f:
        md_text = f.read().decode('utf-8')

    html = markdown.markdown(md_text)

    return render(request, 'project_detail.html', {
        'project': project,
        'content': html
    })



def thought_list(request):
    thought_queryset = Thought.objects.all().order_by('-created_at')
    paginator = Paginator(thought_queryset, 5)  # Show 5 thoughts per page

    page_number = request.GET.get('page')
    thoughts = paginator.get_page(page_number)

    return render(request, 'thoughts/thought_list.html', {'thoughts': thoughts})



def thought_detail(request, slug):
    thought = get_object_or_404(Thought, slug=slug)

    if not thought.markdown_file:
        return HttpResponse("No file uploaded", status=404)

    with thought.markdown_file.open('rb') as f:
        raw_md = f.read().decode('utf-8')


    def convert_obsidian_links(md_text):

        # 1. Full video embeds — only if no extension is given (e.g. ![[video]])
        md_text = re.sub(
            r'!\[\[([^\[\]\.]+)\]\]',  # Matches ![[filename]] with no extension
            r'<video controls width="100%"><source src="/media/thoughts/\1.mp4" type="video/mp4"></video>',
            md_text
        )

        # 2. Image embeds — matches .png, .jpg, .jpeg, .gif, .webp etc.
        md_text = re.sub(
            r'!\[\[([^\[\]]+\.(png|jpg|jpeg|gif|webp))\]\]',
            r'![Image](/media/thoughts/\1)',
            md_text
        )

        # 3. Video/audio inside src="![[...]]" HTML (fallback for <source>)
        md_text = re.sub(
            r'src="!\[\[([^\[\]]+)\]\]"',
            r'src="/media/thoughts/\1"',
            md_text
        )

        return md_text

    cleaned_md = convert_obsidian_links(raw_md)
    html = markdown.markdown(cleaned_md, extensions=['extra'])

    return render(request, 'thoughts/thought_detail.html', {
        'thought': thought,
        'content': html
    })

