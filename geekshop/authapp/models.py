from datetime import timedelta

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class ShopUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name='логин',
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    avatar = models.ImageField(upload_to='users_avatars', blank='True')
    date_birthday = models.DateField(verbose_name='дата рождения')
    first_name = models.CharField(verbose_name='имя', max_length=150)
    last_name = models.CharField(verbose_name='фамилия', max_length=150)
    email = models.EmailField(_('email address'))

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
