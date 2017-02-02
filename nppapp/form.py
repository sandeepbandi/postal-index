from django import forms
 
class UserForm(forms.Form):
    PINCODE = forms.CharField(max_length=100)

