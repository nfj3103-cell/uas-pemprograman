from django import forms
from django.contrib.auth.models import User
from .models import Profile



class RegisterForm(forms.Form):


    nama = forms.CharField(
        max_length=100,
        label="Nama Lengkap"
    )


    no_hp = forms.CharField(
        max_length=15,
        label="Nomor HP"
    )


    email = forms.EmailField(
        label="Email"
    )


    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )



    def clean_email(self):

        email = self.cleaned_data["email"]


        if User.objects.filter(username=email).exists():

            raise forms.ValidationError(
                "Email sudah digunakan."
            )


        return email



    def clean_password(self):

        password = self.cleaned_data["password"]


        if len(password) < 8:

            raise forms.ValidationError(
                "Password minimal 8 karakter."
            )


        return password





    def save(self):


        nama = self.cleaned_data["nama"]

        no_hp = self.cleaned_data["no_hp"]

        email = self.cleaned_data["email"]

        password = self.cleaned_data["password"]



        user = User.objects.create_user(

            username=email,

            email=email,

            first_name=nama,

            password=password

        )



        Profile.objects.create(

            user=user,

            no_hp=no_hp,

            role="CUSTOMER"

        )


        return user