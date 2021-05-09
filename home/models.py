from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# post and user => one to many relationship
# one user can have 0 more posts

class Post(models.Model):
    # aici definim clasa unui 'post'
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # the next line creates one to many relationship
    # "on_delete=models.CASCADE" => deletes the posts if the user is deleted, but not the other way around
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # last modified field = models.DateTimeField(auto_now=True)
    # face update la data modificarii

    def __self__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk' : self.pk})
