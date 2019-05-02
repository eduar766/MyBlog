from django.contrib import admin
from .models import Category, Author, Post, Comment

admin.site.register(
    {
        Category, Author, Post, Comment
    }
)