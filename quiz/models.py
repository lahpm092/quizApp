from django.db import models

# Create your models here.
class Quiz(models.Model):
    topic = models.TextField()
    score = models.IntegerField()
    def __str__(self):
        return self.topic

class Question(models.Model):
    q = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    count = models.IntegerField()
    def __str__(self):
        return self.q

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    explanation = models.TextField()
    def __str__(self):
        return self.answer
