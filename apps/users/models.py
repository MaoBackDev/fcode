from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', max_length=255, unique=True)
    first_name = models.CharField('Nombres', max_length=50, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    avatar = models.ImageField('Imagen', upload_to='profile/', max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # def get_absolute_url(self):
    #     return reverse('', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.email}'