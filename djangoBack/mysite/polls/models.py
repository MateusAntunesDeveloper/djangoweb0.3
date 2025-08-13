from django.db import models
import _datetime
from django.utils import timezone
# Create your models here.

class Quest(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()
    - _datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Quest, on_delete=models.CASCADE)
    text_choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.text_choice