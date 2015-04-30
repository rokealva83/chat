# -*- coding: utf-8 -*-

from django.shortcuts import render
from chat.models import Message
from django.http import JsonResponse


def home(request):
    message = Message.objects.all()
    if message:
        last_id = Message.objects.last().pk
        need_id = int(last_id) - 32
        messages = Message.objects.filter(id__gte=need_id).all()
    else:
        message = Message(
            user='System',
            text='Hello, user'
        )
        message.save()
        messages = Message.objects.all()

    return render(request, "chat.html", {'messages': messages})


def send_message(request):
    user = request.POST.get('user')
    text = request.POST.get('text')
    message = Message(
        user=user,
        text=text
    )
    message.save()


def update_message(request):
    id = int(request.POST.get('id'))
    messages = Message.objects.filter(id__gte=id).all()
    response = []
    for msg in messages:
        response.append({
            'id': msg.pk,
            'text': msg.text,
            'user': msg.user,
        })
    return JsonResponse({
        'result': response
    })


