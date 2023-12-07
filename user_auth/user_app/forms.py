from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','profile_picture', 'user_type', 'address_line1', 'city', 'state', 'pincode')
        
