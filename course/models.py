from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from university.models import *
from django.conf import settings


class Course(models.Model):
    Yr_CHOICES = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
    )
 
    Sem_CHOICES = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Recess'),
    )
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    code = models.CharField(max_length=10, null=False, blank=False)
    year = models.CharField(max_length=10, null=False, blank=False, choices=Yr_CHOICES)
    semester = models.CharField(max_length=10, null=False, blank=False, choices=Sem_CHOICES)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_enroled', blank=True)
 

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.code)
        super(Course, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('course_detail_document_list', args=[self.slug, self.id])
    
    def get_enroll_url(self):
        return reverse('course-enroll', args=[self.slug, self.id])
