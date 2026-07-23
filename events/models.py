from django.db import models


class Event(models.Model):

    STATUS_CHOICES = (

        ('AKTIF','Aktif'),
        ('SELESAI','Selesai'),

    )


    nama_event = models.CharField(
        max_length=200
    )


    deskripsi = models.TextField()


    tanggal = models.DateField()


    lokasi = models.CharField(
        max_length=200
    )


    gambar = models.ImageField(
        upload_to='event/',
        blank=True,
        null=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AKTIF'
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.nama_event