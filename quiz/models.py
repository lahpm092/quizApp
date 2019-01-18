from django.db import models
from datetime import date
# Create your models here.

class Question(models.Model):
    q = models.TextField(default='')
    timesViewed = models.IntegerField(default=0)
    lastJump = models.IntegerField(default=0)
    lastViewed = models.DateField(auto_now_add=True)
    right_answer = models.TextField(default='')
    wrong_answer1 = models.TextField(default='')
    wrong_answer2 = models.TextField(default='')
    wrong_answer3 = models.TextField(default='')

    def __str__(self):
        return self.q
