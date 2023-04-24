from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(recipient_email):
    subject = 'Registration Confirmation'
    message = 'Thank you for registering!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [recipient_email]
    send_mail(subject, message, from_email, recipient_list)