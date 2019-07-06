from django.contrib import admin
from . import models

@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']
    list_filter = ['name', 'abbreviation']
    prepopulated_fields =  {'slug':('name', 'abbreviation')}

@admin.register(models.Collage)
class CollageAdmin(admin.ModelAdmin):

    list_display =['name', 'abbreviation']
    list_filter = ['name', 'abbreviation']
    prepopulated_fields = {'slug':('name', 'abbreviation')}
 

@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'durations', 'abbreviation',]
    list_filter = ['name', 'abbreviation', 'durations']
    prepopulated_fields = {'slug':('name', 'abbreviation')}
