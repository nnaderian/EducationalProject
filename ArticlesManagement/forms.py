from django import forms
from .models import UserProfile, Article
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username' , 'email' , 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'birthdate', 'picture')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'AuthorName', 'type', 'publication_date')