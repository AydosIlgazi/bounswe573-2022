from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from tinymce import models as tinymce_models



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Test(models.Model):
    testId = models.CharField(max_length=100)


class LearningSpace(models.Model):
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    short_description = models.CharField(max_length=350, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=300, blank=True)


class Topic(models.Model):
    title = models.CharField(max_length=200)
    content = tinymce_models.HTMLField()
    duration = models.DateField()
    learning_space = models.ForeignKey(LearningSpace, on_delete=models.CASCADE)