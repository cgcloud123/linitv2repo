from dataclasses import fields
import email
from socket import fromshare
from tkinter import Widget
from .models import Userdetails
from django import forms
from linitapp.models import *

# from app.models import Employee

class CustForm(forms.ModelForm):
    name = forms.CharField(max_length=500,label='', widget=forms.TextInput(attrs={'placeholder':'Full Name*','size': '10', 'class':'form-control no-border'}))
    email = forms.CharField(max_length=500,label='', widget=forms.EmailInput(attrs={'placeholder':'Email*','size': '10','class':'form-control no-border'}))
    contact_no = forms.CharField(max_length=500,label='', widget=forms.NumberInput(attrs={'placeholder':'Contact No*','size': '10','class':'form-control no-border'}))
    description = forms.CharField(max_length=500,label='', widget=forms.TextInput(attrs={'placeholder':'Description*','size': '10','class':'form-control no-border'}))

    class Meta:
        model = Userdetails
        fields = "__all__"
      
