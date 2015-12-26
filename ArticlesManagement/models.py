# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    birthdate = models.DateField()
    picture = models.ImageField(upload_to='profile_images')

class Article(models.Model):
    title = models.CharField(max_length=100)
    AuthorName = models.CharField(max_length=50)
    publication_date = models.DateField()
    created_date = models.DateTimeField(default=None)
    RESEARCH_ACADEMIC = 'RA'
    ANALYTICAL = 'AN'
    OTHER = 'OT'
    TYPE_CHOICES = (
        (RESEARCH_ACADEMIC, 'علمی پژوهشی'),
        (ANALYTICAL, 'تحلیلی'),
        (OTHER, 'سایر'),
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=RESEARCH_ACADEMIC)
    def get_type_value(self):
        if self.type == 'RA':
            return 'علمی پژوهشی'
        elif self.type == 'AN':
            return 'تحلیلی'
        else:
            return 'سایر'

    def get_publication_date_value(self):
        print '**'
        date_value = str(self.publication_date.day)
        print '1'
        print date_value
        months = {'01': 'فروردین', '02': 'اردیبهشت' , '03':'خرداد' , '04': 'تیر', '05': 'مرداد', '06': 'شهریور', '07':'مهر', '08': 'آبان', '09':'آذر', '10':'دی', '11':'بهمن', '12':'اسفند',}
        date_value+=' '
        print '2'
        print self.publication_date.month
        print months

        date_value+= months[self.publication_date.month]
        print '%%'
        print date_value
        date_value+=' '
        date_value+=str(self.publication_date.year)
        return  date_value







