from django import forms
from django.contrib.auth.models import User
from book_app.models import custom_user, Sell

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = custom_user
        fields = ['firstname','lastname','username','email','user_pin','phone','password']

class SellForm(forms.ModelForm):
    class Meta:
        model=Sell
        fields=['book_name','author','published_by','tags','types','discount','price','pin_code','description','photo']
