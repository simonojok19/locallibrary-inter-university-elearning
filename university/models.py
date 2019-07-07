from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

"""
    This is the module for storing information about the university
"""
class University(models.Model):
    name            = models.CharField(max_length=50, null=False, blank=False, unique=True)
    abbreviation    = models.CharField(max_length=10, null=False, blank=False)
    description     = models.TextField()
    slug            = models.SlugField(max_length=50, unique=True)
    picture         = models.ImageField(upload_to='university/picture/%Y/%m/%d', null=True, blank=True)
    display_picture = models.ImageField(upload_to='university/display_picture/%Y/%m/%d', null=True, blank=True)
    address         = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.address)
        
        super(University, self).save(*args, **kwargs)

class Collage(models.Model): 
    university = models.ForeignKey(University, related_name='university_collages', on_delete=models.CASCADE)
    name            = models.CharField(max_length=50, null=False, blank=False, unique=True)
    abbreviation    = models.CharField(max_length=10, null=False, blank=False)
    description     = models.TextField()
    slug            = models.SlugField(max_length=50, unique=True)
    picture         = models.ImageField(upload_to='university/picture/%Y/%m/%d', null=True, blank=True)
    display_picture = models.ImageField(upload_to='university/display_picture/%Y/%m/%d', null=True, blank=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.abbreviation)
        super(Collage, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('collage_detail', args=[self.slug, self.id])

class Program(models.Model):
    collage         = models.ForeignKey(Collage, on_delete=models.CASCADE)
    name            = models.CharField(max_length=50, null=False, blank=False, unique=True)
    abbreviation    = models.CharField(max_length=10, null=False, blank=False)
    description     = models.TextField()
    slug            = models.SlugField(max_length=50, unique=True)
    display_picture = models.ImageField(upload_to='program/display_picture/%Y/%m/%d', null=True, blank=True)
    durations       = models.PositiveIntegerField()
    slug            = models.SlugField(max_length=50, unique=True)
 

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.abbreviation)
        super(Program, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('course_list_program_detail', args=[self.slug, self.id])

