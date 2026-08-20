from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Create password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Confirm password'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Phone number'}))
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control custom-input', 'rows': 3, 'placeholder': 'Delivery address'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Choose username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Email address'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control custom-input'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control custom-input'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control custom-input'}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control custom-input'}))
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control custom-input', 'rows': 3}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        user_profile = kwargs.pop('profile', None)
        super().__init__(*args, **kwargs)
        if user_profile:
            self.fields['phone_number'].initial = user_profile.phone_number
            self.fields['address'].initial = user_profile.address
