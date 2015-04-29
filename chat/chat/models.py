# -*- coding: utf-8 -*-

from django.db import models


class Message(models.Model):
    user = models.CharField(max_length=32)
    text = models.CharField(max_length=512)

