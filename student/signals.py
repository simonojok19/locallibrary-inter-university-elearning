from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from . import models

@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    models.Profile.objects.create(user=user)