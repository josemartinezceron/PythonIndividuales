from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    TZ = [
        ("EU", "EUROPE"),
        ("US", "UNITED STATES")

    ]
    title = models.CharField(verbose_name="Titulo del Posteo", max_length=100)
    content = models.TextField(verbose_name="Texto del Posteo")
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tzone = models.CharField(choices=TZ, verbose_name="Zona Horaria")

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title + '-by ' + self.user.username
