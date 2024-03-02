from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email',
                  'description', 'category', 'picture')


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, min_length=3)
    last_name = forms.CharField(required=True, min_length=3)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError(
                'Email already exist', code='invalid'))

        return email
