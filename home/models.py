# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    misafirhaneler = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Odalar(models.Model):

    #__Odalar_FIELDS__
    baslik = models.CharField(max_length=255, null=True, blank=True)

    #__Odalar_FIELDS__END

    class Meta:
        verbose_name        = _("Odalar")
        verbose_name_plural = _("Odalar")


class Musteriler(models.Model):

    #__Musteriler_FIELDS__
    adisoyadi = models.CharField(max_length=255, null=True, blank=True)

    #__Musteriler_FIELDS__END

    class Meta:
        verbose_name        = _("Musteriler")
        verbose_name_plural = _("Musteriler")


class Kasa(models.Model):

    #__Kasa_FIELDS__
    islem = models.IntegerField(null=True, blank=True)

    #__Kasa_FIELDS__END

    class Meta:
        verbose_name        = _("Kasa")
        verbose_name_plural = _("Kasa")



#__MODELS__END
