from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-pub_date',)

    def __unicode__(self):
        return self.title

class Count(models.Model):
    year=models.CharField(max_length=4)
    name=models.CharField(max_length=20)
    price=models.PositiveIntegerField()
    count=models.CharField(max_length=4)
    last=models.CharField(max_length=4)

    def __unicode__(self):
        return self.name

