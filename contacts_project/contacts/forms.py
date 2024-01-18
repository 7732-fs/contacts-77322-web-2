from django import forms 
from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.Form):
    name=forms.CharField(max_length=6)
    email=forms.EmailField(required=True)

class ContactFormFromModel(ModelForm):
    class Meta:
        model = Contact
        fields="__all__"
        