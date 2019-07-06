from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    display_picture = models.ImageField(upload_to='user/dp/display_picture/%Y/%m/%d', null=True, blank=True)
    picture         = models.ImageField(upload_to='user/wall/picture/%Y/%m/%d', null=True, blank=True)
    bio             = models.TextField()

    def __str__(self):
        return self.user.username


