from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile

class UpdateUserInfoForm(forms.ModelForm):
  phone = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your phone number'}), required=False)
  address1 = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you address 1'}), required=False)
  address2 = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you address 2'}), required=False)
  city = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you city'}), required=False)
  state = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you state'}), required=False)
  zipcode = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you zipcode'}), required=False)
  country = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you country'}), required=False)

  class Meta:
    model = Profile
    fields = ['phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country']

class UserUpdatePasswordForm(SetPasswordForm):
  new_password1 = forms.CharField(label="", max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'name': 'password',
                                                                  'type': 'password',
                                                                  'placeholder': 'enter you password'}))
  new_password2 = forms.CharField(label="", max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'name': 'password',
                                                                  'type': 'password',
                                                                  'placeholder': 'enter you password again'}))
  class Meta:
    model = User
    fields = ['new_password1', 'new_password2']

class UserUpdateForm(UserChangeForm):
  password = None
  first_name = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you name'}), required=False)
  last_name = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you lastname'}), required=False)


  email = forms.EmailField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you email'}))
  username = forms.CharField(label="", max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you username'}))

  class Meta:
    model = User
    fields = ['first_name', 'last_name','username', 'email']


class SignupForm(UserCreationForm):
  first_name = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you name'}))
  last_name = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you lastname'}))


  email = forms.EmailField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you email'}))
  username = forms.CharField(label="", max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you username'}))

  password1 = forms.CharField(label="", max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'name': 'password',
                                                                  'type': 'password',
                                                                  'placeholder': 'enter you password'}))
  password2 = forms.CharField(label="", max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'name': 'password',
                                                                  'type': 'password',
                                                                  'placeholder': 'enter you password again'}))

  class Meta:
    model = User
    fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']