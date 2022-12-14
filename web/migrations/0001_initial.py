# Generated by Django 4.1.1 on 2022-09-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.TextField(max_length=4096, verbose_name='content')),
                ('created', models.DateField(auto_now=True, verbose_name='created')),
                ('updated', models.DateField(auto_now_add=True, verbose_name='updated')),
                ('publicated', models.BooleanField(default=False)),
            ],
        ),
    ]
