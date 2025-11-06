from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    extra_info = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # bu sahə olmalıdır
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now