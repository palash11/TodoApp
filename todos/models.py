# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User

class Todo(models.Model):
    taskName = models.CharField(max_length=200, unique=True, blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    isDone = models.BooleanField()
    doneAt = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('users.User', related_name='todos', on_delete=models.CASCADE, null=False)
