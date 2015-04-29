# -*- coding: utf-8 -*-

from django.shortcuts import render
from chat.models import Message

def home(request):
    messages = Message.objects.all()
    return render(request, "chat.html", {'messages':messages})


def send_message(request):
    user = request.POST.get('user')
    text = request.POST.get('text')
    message = Message(
        user = user,
        text = text
    )
    message.save()
    messages = Message.objects.all()
    return render(request, "chat.html", {'messages':messages})


# def message():