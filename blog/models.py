from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now) # timezone.now is a function but we don't put () because we don't wanna execute it, just have to reference the function
    author = models.ForeignKey(User, on_delete=models.CASCADE) # delete post if author is deleted
