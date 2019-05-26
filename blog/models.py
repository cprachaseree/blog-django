from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)                   # Character Field
    content = models.TextField()                               # multiple lines
    date_posted = models.DateTimeField(default=timezone.now)   # timezone.now is a function
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if the user gets deleted then delete post

    def __str__(self):
        return f"{self.title} by {self.author} on {self.date_posted}"
