from django import forms
from .models import *
  
class RegisterForm(forms.ModelForm):
  
    class Meta:
        model = Register
        fields = [ "firstname","lastname","Profilepicture","username","email","password","confirmpassword","address_line","address_city","address_state","address_pincode"]
        