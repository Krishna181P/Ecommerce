from django import forms
from django.contrib.auth.models import User
from ecommerce.models import Cart,OrderPlaced


class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Fisrt Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email@gmail.com'}),

        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }

class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=['quantity']
        widgets={
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
        }
class OrderForm(forms.ModelForm):
    class Meta:
        model=OrderPlaced
        fields=['address','email']
        widgets={
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
       