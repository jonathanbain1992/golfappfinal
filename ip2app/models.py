# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=30)
    quiz_question = models.CharField(max_length=30)
