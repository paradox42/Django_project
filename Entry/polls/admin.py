# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):

    list_display = ('id','question_title', 'question_text')

    readonly_fields = ('id',)

    search_fields = ['question_text']


admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)
