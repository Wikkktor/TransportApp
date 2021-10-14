from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    labels = {
        'username': ' ',
        'password': ' '
    }


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'password'}),
            'email': forms.TextInput(attrs={'placeholder': 'example@email.com'})
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


