from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import hello.templates
import telebot
import requests

bot = telebot.TeleBot("6805524954:AAF1LHY_DOAUQ6kbSO0yrMyiEeO_4F7enqQ")
def send_message(text: str):
    token = "6805524954:AAF1LHY_DOAUQ6kbSO0yrMyiEeO_4F7enqQ"
    url = "https://api.telegram.org/bot"
    channel_id = "@diagxpert_channel"
    url += token
    method = url + "/sendMessage"
    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")


def send_contact_email_message(subject, email, content, ip, user_id):
    """
    Function to send contact form email
    """
    user = User.objects.get(id=user_id) if user_id else None
    message = render_to_string('feedback_email_send.html', {
        'email': email,
        'content': content,
        'ip': ip,
        'user': user,
    })
    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, ['vak2004@list.ru'])
    email.send(fail_silently=False)
    bot.send_message(5048075977, message)
    send_message(message)
