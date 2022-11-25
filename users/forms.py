from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

user_model = get_user_model()

class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    
    class Meta:
        model = user_model
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {
            'username': None,
        }
        
    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    