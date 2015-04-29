# -*- coding: utf-8 -*-

from django.shortcuts import render
from chat.models import Message

def home(request):
    messages = Message.objects.all()

    return render(request, "chat.html", {'messages':messages})