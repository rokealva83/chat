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


def update_message(request):
    id = int(request.POST.get('id'))
    messages = Message.objects.filter(id__gr=id)
    a=4