from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='title'
    )
    content = models.TextField(
        max_length=4096, verbose_name='content'
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='created'
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='updated'
    )
    publicated = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('datailnews', kwargs={'news_id': self.pk})
