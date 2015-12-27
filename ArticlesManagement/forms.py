# -*- coding: utf-8 -*-
from django import forms
from .models import UserProfile, Article
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    my_username_errors = {
        'required': 'فیلد اجباری',
        'invalid': 'نامعتبر',
        'unique': 'نام کاربری تکراری'
    }
    my_errors_default = {
        'required': 'فیلد اجباری'
    }

    username = forms.CharField(error_messages=my_username_errors)
    password = forms.CharField(error_messages=my_errors_default,widget=forms.PasswordInput())
    email = forms.CharField(error_messages=my_errors_default)

    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['password'].label = 'رمز عبور'
        self.fields['email'].label = 'پست الکترونیک'




    class Meta:
        model = User
        fields = ('username' , 'email' , 'password')

class UserProfileForm(forms.ModelForm):
    my_errors_default = {
        'required': 'فیلد اجباری'
    }
    my_picture_errors = {
        'required': 'فیلد اجباری',
        'empty': 'عکس نباید خالی باشد'
    }
    first_name = forms.CharField(error_messages=my_errors_default)
    last_name = forms.CharField(error_messages=my_errors_default)
    phone_number = forms.CharField(error_messages=my_errors_default)
    birthdate = forms.DateField(error_messages=my_errors_default)
    picture = forms.FileField(error_messages=my_picture_errors)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].label = 'نام'
        self.fields['last_name'].label = 'نام خانوادگی'
        self.fields['phone_number'].label = 'شماره تماس'
        self.fields['birthdate'].label = 'تاریخ تولد'
        self.fields['picture'].label = 'عکس خود را آپلود کنید'



    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone_number', 'birthdate', 'picture')

class ArticleForm(forms.ModelForm):
    my_errors_default = {
        'required': 'فیلد اجباری'
    }
    title = forms.CharField(error_messages=my_errors_default)
    AuthorName = forms.CharField(error_messages=my_errors_default)
    publication_date = forms.DateField(error_messages=my_errors_default)


    def __init__(self, *args, **kwargs):
        super(ArticleForm,self).__init__(*args, **kwargs)
        self.fields['title'].label = 'عنوان مقاله'
        self.fields['AuthorName'].label = 'نام نویسنده'
        self.fields['type'].label = 'نوع مقاله'
        self.fields['publication_date'].label = 'تاریخ انتشار'

    class Meta:
        model = Article
        fields = ('title', 'AuthorName', 'type', 'publication_date')