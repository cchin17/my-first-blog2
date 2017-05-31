from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model): #define object model Post, models.Model means that the Post is a Django model, django will save to database
    #define properties
    author = models.ForeignKey('auth.User') #link to another model
    title = models.CharField(max_length=200) #define text with a limited number of chars
    text = models.TextField() #used for long text without limit
    created_date = models.DateTimeField(default=timezone.now) #date and time
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
