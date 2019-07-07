from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'semester', 'program']
    list_filter = ['program', 'name']
    prepopulated_fields = {'slug':('name', 'code')} 