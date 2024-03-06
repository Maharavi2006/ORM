from django.db import models
from django.contrib import admin
class Book(models.Model):
        author_name=models.CharField(max_length=20);
        author_details=models.CharField(max_length=40);
        book_title=models.CharField(max_length=30);
        publication=models.DateField();
        book_version=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
        list_display=("author_name","author_details","book_title","publication","book_version");
