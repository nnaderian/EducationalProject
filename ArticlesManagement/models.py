# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=10, verbose_name='شماره تماس')
    birthdate = models.DateField(verbose_name='تاریح تولد')
    picture = models.ImageField(upload_to='profile_images', verbose_name='عکس خود را آپلود کنید')


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان مقاله')
    AuthorName = models.CharField(max_length=50, verbose_name='نام نویسنده')
    publication_date = models.DateField(verbose_name='تاریخ انتشار')
    created_date = models.DateTimeField(default=None)
    creator_id = models.IntegerField(default=0)
    RESEARCH_ACADEMIC = 'RA'
    ANALYTICAL = 'AN'
    OTHER = 'OT'
    TYPE_CHOICES = (
        (RESEARCH_ACADEMIC, 'علمی پژوهشی'),
        (ANALYTICAL, 'تحلیلی'),
        (OTHER, 'سایر'),
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=RESEARCH_ACADEMIC, verbose_name='نوع مقاله')

    def get_type_value(self):
        if self.type == 'RA':
            return 'علمی پژوهشی'
        elif self.type == 'AN':
            return 'تحلیلی'
        else:
            return 'سایر'

    def __unicode__(self):
        return self.title
