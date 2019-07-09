from django.db import models
from django.utils.safestring import mark_safe


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    banner = models.ImageField(upload_to="magic_number/static/magic_number")

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    birthday_input = models.DateTimeField('birthday')
    avatar = models.IntegerField(default=0)

    def __str__(self):
        return self.birthday_input
