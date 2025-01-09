from django import forms
from .models import store,Checkout,Feedback

class ContactForm(forms.ModelForm):
    class Meta:
        model=store
        fields=['username','email','message']
class Checkout_form(forms.ModelForm):
    class Meta:
        model=Checkout
        fields=['full_name','email','address','street','state','phone']



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['category', 'feedback']  # Specify the fields to include in the form
        labels = {
            'category': 'Chai Type',
            'feedback': 'Your Feedback',
        }
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'feedback': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your feedback here...',
                'rows': 5,
            }),
        }
