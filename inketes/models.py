from django.db import models
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("Data de publicação")
    def __str__(self):
        return f'{self.question_text}'
    def nova(self):
        return self.pub_date >= datetime.timezone.now() - datetime.timedelta(hours=24)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.choice_text}'