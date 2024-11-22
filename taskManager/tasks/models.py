from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils.timezone import now, timedelta

def invite_expiration():
    return now() + timedelta(days=7)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Invite(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=32, unique=True, default=get_random_string)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=invite_expiration)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_expired(self):
        return now() > self.expires_at