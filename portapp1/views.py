# portapp1/views.py
from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, BlogPost
import html

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    posts = BlogPost.objects.all().order_by('-published_date')
    return render(request, 'portapp1/home.html', {'projects': projects, 'skills': skills,'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    # Only escape specific fields that contain user-generated content
    content = html.escape(post.content)  # Assuming 'content' is the field containing user-generated content
    return render(request, 'portapp1/blog_detail.html', {'post': post, 'content': content})