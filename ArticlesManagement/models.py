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

    def __unicode__(self):
        return u'%s %s' %(self.first_name, self.last_name)

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

    def __unicode__(self):
        return self.title







