# -*- coding: utf-8 -*-
from django import forms
from .models import UserProfile, Article
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    my_default_errors = {
        'required': 'قسمت اجباری',
        'invalid': 'نامعتبر',
        'unique': 'تکراری'
    }
    first_name = forms.CharField(required=True, error_messages=my_default_errors)
    last_name = forms.CharField(required=True, error_messages=my_default_errors)
    email = forms.EmailField(required=True, error_messages=my_default_errors)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['password'].label = 'رمز عبور'
        self.fields['email'].label = 'پست الکترونیک'
        self.fields['first_name'].label = 'نام'
        self.fields['last_name'].label = 'نام خانوادگی'
        self.fields['username'].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
        error_messages = {}
        error_messages.update(dict.fromkeys(['username', 'password'], {
            'required': 'قسمت اجباری',
            'invalid': 'نامعتبر',
            'unique': 'تکراری'
        }))


class UserProfileForm(forms.ModelForm):
    forms.DateInput.input_type = "date"
    phone_number = forms.CharField(required=False, label=UserProfile._meta.get_field_by_name('phone_number')[0].
                                   verbose_name)
    picture = forms.FileField(required=False, label=UserProfile._meta.get_field_by_name('picture')[0].verbose_name)

    class Meta:
        model = UserProfile
        fields = ('phone_number', 'birthdate', 'picture')
        error_messages = {
            'birthdate': {
                'required': 'قسمت اجباری',
                'empty': 'نباید خالی باشد'
            }
        }


class ArticleForm(forms.ModelForm):

    forms.DateInput.input_type = "date"

    class Meta:
        model = Article
        fields = ('title', 'AuthorName', 'type', 'publication_date')
        error_messages = {}
        error_messages.update(dict.fromkeys(['title', 'AuthorName', 'type', 'publication_date'], {
            'required': 'قسمت اجباری',
            'invalid': 'نامعتبر',
            'unique': 'تکراری'
        }))
