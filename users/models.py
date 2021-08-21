# from django.db import models


# this code needs to be executed by the python interpreter that's why it's in ``models.py``

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

# Added following signal for sending email
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        "Password Reset for {title}".format(title="Some website title"),        # title
        email_plaintext_message,        # message
        "noreply@somehost.local",           # from
        [reset_password_token.user.email]        # to
    )