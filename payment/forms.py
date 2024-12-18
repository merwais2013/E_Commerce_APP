from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
  shipping_full_name = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your full name'}), required=True)
  shipping_email = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your email'}), required=True)

  shipping_phone = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your phone number'}), required=True)
  shipping_address1 = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you address 1'}), required=True)
  shipping_address2 = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you address 2'}), required=False)
  shipping_city = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you city'}), required=True)
  shipping_state = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you state'}), required=False)
  shipping_zipcode = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you zipcode'}), required=False)
  shipping_country = forms.CharField(label="", max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter you country'}), required=True)

  class Meta:
    model = ShippingAddress
    fields = ['shipping_full_name', 'shipping_email', 'shipping_phone', 'shipping_address1',
              'shipping_address2', 'shipping_state', 'shipping_city', 'shipping_zipcode', 'shipping_country']
    exclude= ['user',]