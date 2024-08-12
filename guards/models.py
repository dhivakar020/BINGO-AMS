from django.db import models
from django.contrib.auth.models import User


class Attendance(models.Model):
    guard = models.ForeignKey(User, on_delete=models.CASCADE)
    selfie = models.ImageField(upload_to='selfies/')
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.guard.username} - {self.timestamp}"
