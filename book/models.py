from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from university.models import *
from course.models import Course

class BookRequest(models.Model):
    requestee       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_requests')
    title           = models.CharField(max_length=100, null=False, blank=False)
    descriptions    = models.TextField()
    created         = models.DateTimeField(auto_now_add=True)
    slug            = models.SlugField(max_length=50, unique=True)
    program         = models.ForeignKey(Program, on_delete=models.CASCADE)
    course          = models.ForeignKey(Course, on_delete=models.CASCADE)
    uploaded        = models.BooleanField(default=False)
    upload_times    = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, self.id)
        
        if self.upload_times >= 5:
            self.uploaded = True
        
        return super(BookRequest, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('request_detail_doc_upload', args=[self.slug, self.id])

class Book(models.Model):
    title               = models.CharField(max_length=50, unique=True, blank=False, null=False)
    extention           = models.CharField(max_length=5, blank=True)
    uploaded            = models.DateTimeField(auto_now_add=True)
    file                = models.FileField(upload_to='files/%Y/%m/%d', blank=False, null=False)
    slug                = models.SlugField(max_length=50)
    course              = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    contributor         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descriptions        = models.TextField()
    downloads           = models.PositiveIntegerField(default=0)
    views               = models.PositiveIntegerField(default=0)
    book_request    = models.ForeignKey(BookRequest, on_delete=models.SET_NULL, null=True, blank=True)
    program             = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, self.id)
        if not self.extention:
            self.extention = str(self.file).rsplit('.', 1)[1].lower()
        return super(Book, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document', args=[self.slug, self.pk])

    def get_download_url(self):
        return reverse('download', args=[self.slug, self.pk])
    
 