from django import forms
from .models import store

class contact(forms.ModelForm):
    class Meta:
        model=store
        field=['name','email','meassage']
