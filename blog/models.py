from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    # setting the title of the article with max_length of 100 characters
    title = models.CharField(max_length=100)
    # this will help in the content of the article
    content = models.TextField()
    # setting the date and time field as default as we will need the updated time for the post
    date_posted = models.DateTimeField(default=timezone.now)
    # one user can have many post so we use ForeignKey, and on delete of user his/her post will also deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


