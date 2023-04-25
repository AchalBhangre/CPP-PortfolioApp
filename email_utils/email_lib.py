from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(recipient_email):
    subject = 'Registration Confirmation with Portfolio Site'
    message = 'Thank you for registering with Us!, Hope you enjoy the Site.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [recipient_email]
    send_mail(subject, message, from_email, recipient_list)