from django import forms
from .models import store

class ContactForm(forms.ModelForm):
    class Meta:
        model=store
        fields=['username','email','message']
