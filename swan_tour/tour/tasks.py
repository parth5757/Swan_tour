import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','swan_tour.settings')

django.setup()

from core.models import Contact
from swan_tour import settings

from celery import shared_task
from django.core.mail import send_mail
@shared_task(bind=True)
def test_func(self):
    print("Test function")
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def send_contact_func(self):
    # last added in model
    contact = Contact.objects.latest('id')
    mail_subject = "we received your contact"
    message = "we started to working on this as soon as possible someone from our team member get back to you\n" "your message: " + contact.message
    to_email = contact.email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    print("From", settings.EMAIL_HOST_USER)

