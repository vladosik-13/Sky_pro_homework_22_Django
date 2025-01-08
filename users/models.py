from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    username_validator = None
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    phone_number = models.CharField(max_length=35, unique=True, null=True, blank=True, verbose_name=_('Phone Number'))
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, verbose_name=_('Avatar'))
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Country'))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # Переопределение полей с добавлением related_name
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_set',  # Уникальное имя для обратного доступа
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_set',  # Уникальное имя для обратного доступа
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )