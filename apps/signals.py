from django.core.mail import send_mail
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.http import JsonResponse

from apps.models import User
from apps.models.users import DeletedUsers


@receiver(post_delete, sender=User)
def my_handler(sender, instance: User, **kwargs):
    DeletedUsers.objects.create(phone_number=instance.phone_number, type=instance.type)


@receiver(post_save, sender=User)
def notifiy_user(sender, instance: User, created, **kwargs):
    if created:
        subject = 'Registeration'
        message = f'User: {instance.phone_number} successfully registered!'
        email = 'jasurbekbekmirzayev2004@gmail.com'
        send_mail(subject=subject, message=message, from_email=email, recipient_list=[email, ])
        return JsonResponse({"message": "ketti"})
