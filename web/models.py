from django.db import models
from django.urls import reverse
from blog.settings import AUTH_USER_MODEL


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
    author = models.ForeignKey(
        AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name='author', 
        related_name='author',
        null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('datailnews', kwargs={'news_id': self.pk})

class Images(models.Model):
    '''
        news -> House
        image
    '''
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='web/images/%Y/%m/%d/%H')

    def __str__(self):
        return self.news

    def get_absolute_url(self):
        return reverse('images', kwargs={'pk': self.pk})