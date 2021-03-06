from operator import mod
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from tinymce import models as tinymce_models
from django.utils.timezone import now




class LearningSpace(models.Model):
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    short_description = models.CharField(max_length=350, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=200)
    content = tinymce_models.HTMLField()
    estimated_time = models.IntegerField(blank=True, null=True, verbose_name="Estimated Completion Time(hours)")
    learning_space = models.ForeignKey(LearningSpace, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Prerequisite(models.Model):
    main_topic = models.ForeignKey(Topic, related_name="main_topic", on_delete=models.CASCADE)
    prerequisite_topic = models.ForeignKey(Topic, related_name="prerequisite_topic" ,on_delete=models.CASCADE)

class Resource(models.Model):
    content = tinymce_models.HTMLField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_date = models.DateField(default=now, editable=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content= models.CharField(max_length=350)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    created_date = models.DateField(default=now, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Notes(models.Model):
    content= models.CharField(max_length=500)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=False)

class LikedResources(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class LearningSpaceParticipation(models.Model):
    learning_space = models.ForeignKey(LearningSpace, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)