from django.db import models
from django.contrib.auth.models import User


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
class Ticket(models.Model):

    CATEGORY_CHOICES = (

        ('REGULER', 'Reguler'),
        ('VIP', 'VIP'),

    )


    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='tickets'
    )


    nama_tiket = models.CharField(
        max_length=100
    )


    kategori = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='REGULER'
    )


    harga = models.IntegerField()


    stok = models.IntegerField(
        default=0
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.nama_tiket
class Booking(models.Model):

    STATUS_CHOICES = (

        ('PENDING', 'Menunggu Pembayaran'),
        ('PAID', 'Sudah Dibayar'),
        ('CANCEL', 'Dibatalkan'),

    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE
    )


    jumlah = models.IntegerField(
        default=1
    )


    total_harga = models.IntegerField()


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.user.username} - {self.ticket.nama_tiket}"