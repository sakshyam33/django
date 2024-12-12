from django import forms
from .models import store,Checkout

class ContactForm(forms.ModelForm):
    class Meta:
        model=store
        fields=['username','email','message']
class Checkout_form(forms.ModelForm):
    class Meta:
        model=Checkout
        fields=['full_name','email','address','street','state','phone']