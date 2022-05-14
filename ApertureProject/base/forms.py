from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person, Ticket

class SignUpForm(UserCreationForm):
    username = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    first_name =forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    last_name=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    email=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    password1=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    password2=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'})

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('Seat_location',
                'Ticket_class',
                'Seat_Number',)