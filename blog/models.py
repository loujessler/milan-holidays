from django.db import models
from django import forms
from django.utils import timezone
from django.utils.timezone import now
from django.db.models import Model
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=1055) # заголовок поста
    image = models.ImageField('Фото', upload_to='blogs_images/') # фото блога
    created = models.DateTimeField('Создан', auto_now_add=True) # дата публикации
    updated = models.DateTimeField('Обновлен', auto_now=True)
    content = models.TextField(max_length=10000) # текст поста

    def __str__(self, *args, **kwargs):
        return "Блог: %s" % (self.title)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-created',]
