from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from hackapp.models import CustomUser


class SignupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[field].help_text = None

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password', 'user_type']


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'type': 'text'}))
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
