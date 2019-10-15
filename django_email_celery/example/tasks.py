from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def email(request):
    sleep(10)
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['kushalbarbhaya@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return None
