from django.contrib import admin
from . import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'contributor', ]
    list_filter = ['title', 'contributor']
    prepopulated_fields = {'slug':('title', 'contributor')}


@admin.register(models.BookRequest)
class BookRequest(admin.ModelAdmin):
    list_display = ('requestee', 'title', 'created', 'course', 'uploaded')
    list_filter = ('requestee', 'course')
    prepopulated_fields = {'slug':('title', 'course')}
