from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Room, Userprofile


# ------------------ ROOM FORM ------------------
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


# ------------------ USER PROFILE FORMS ------------------
class UserProfileForm(forms.ModelForm):
    """Form for creating a full user profile."""
    class Meta:
        model = Userprofile
        fields = ['username', 'email', 'phone', 'profile_image', 'bio']


class CustomUserProfileForm(forms.ModelForm):
    """Form for updating profile-specific fields only."""
    class Meta:
        model = Userprofile
        fields = ['phone', 'profile_image', 'bio']


class UserUpdateForm(forms.ModelForm):
    """Form for updating both user and profile details."""
    class Meta:
        model = Userprofile
        fields = ['username', 'email', 'phone', 'profile_image', 'bio']


# ------------------ AUTH USER FORMS ------------------
class CustomUserForm(forms.ModelForm):
    """Form for registering a User object with username, email, password."""
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserRegistrationForm(forms.ModelForm):
    """Registration form with confirm password field and validation."""
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_confirm")

        if password and confirm_password and password != confirm_password:
            self.add_error("password_confirm", "Passwords do not match")

        return cleaned_data
