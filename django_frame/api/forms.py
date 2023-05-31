from .models import Account
from django import forms



class Form(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['Email_id','Account_id','Account_name','app_secret_token']

