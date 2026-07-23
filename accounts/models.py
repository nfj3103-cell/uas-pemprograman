from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    ROLE_CHOICES = (
        ('CUSTOMER', 'Customer'),
        ('ADMIN', 'Admin'),
        ('PETUGAS', 'Petugas'),
    )


    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


    no_hp = models.CharField(
        max_length=15,
        blank=True
    )
    alamat = models.TextField(
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='CUSTOMER'
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.user.username
    