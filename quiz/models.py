from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions")
    question = models.TextField()
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    correct = models.IntegerField()

    def __unicode__(self):
        return self.quiz.name + " / " + self.question
