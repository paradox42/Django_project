# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question
from django.urls import reverse

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

# Create your tests here.
class QuestionModelTests(TestCase):
    """ was_published_recently() returns False for questions whose pub_date is older than 1 day """
    def test_was_published_recenlty_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.aws_published_recently(), False)

    def test_was_published_recently_with_future_question(self):
        """was_published_recently() return False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

class QuestionindexViewTests(TestCase):
    def test_no_questions(self):
        """if no questions exist, an appropriate message is displayed"""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question(question_text="Past question.", days = -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
