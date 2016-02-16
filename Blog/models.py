# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    image = models.FileField()
    content = models.TextField()
    published = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={"id": self.id})

    class Meta:
        verbose_name = "Yazı"
        verbose_name_plural = "Yazılar"


class AboutAndContact(models.Model):
    about = models.TextField("Hakkımızda")
    contact = models.TextField("İletişim")

    def __unicode__(self):
       return "Bilgiler"

    class Meta:
        verbose_name = "Bilgi"
        verbose_name_plural = "Bilgiler"
