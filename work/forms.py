from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Buyer,Seller,Product
from django.contrib.auth.models import User
class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        exclude = []
class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        exclude = []
class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []