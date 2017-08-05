# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#customized import

from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=100, default="no title")
    question_text = models.CharField(max_length=200, default ="no content")

    def __unicode__(self):
        return self.question_title




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
