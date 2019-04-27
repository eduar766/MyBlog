from django.contrib import admin
from .models import Category, Author, Post

admin.site.register(
    {
        Category, Author, Post
    }
)