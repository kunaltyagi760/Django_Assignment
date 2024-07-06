from django.db import models

# Create your models here.

class Posts(models.Model):
    postId = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title
