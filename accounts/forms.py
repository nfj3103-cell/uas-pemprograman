from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(forms.Form):

    nama = forms.CharField(
        max_length=100
    )

    no_hp = forms.CharField(
        max_length=15
    )

    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput
    )


    def save(self):

        nama = self.cleaned_data['nama']
        no_hp = self.cleaned_data['no_hp']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']


        user = User.objects.create_user(

            username=email,

            email=email,

            password=password,

            first_name=nama

        )


        Profile.objects.create(

            user=user,

            no_hp=no_hp,

            role='CUSTOMER'

        )


        return user