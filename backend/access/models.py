from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AccessPoint(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class AccessEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    person_name = models.CharField(max_length=100, blank=True)  # opcional si no quieres usar User
    access_point = models.ForeignKey(AccessPoint, on_delete=models.CASCADE, related_name='events')
    authorized = models.BooleanField(default=False)
    reason = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        who = self.user.username if self.user else self.person_name or 'Unknown'
        return f"{who} @ {self.access_point} -> {'OK' if self.authorized else 'DENIED'}"
# Create your models here.
