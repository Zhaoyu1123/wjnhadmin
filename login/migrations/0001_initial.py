# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-04 13:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_num', models.CharField(blank=True, default='', max_length=100, verbose_name='\u8eab\u4efd\u8bc1\u53f7')),
                ('phone', models.CharField(blank=True, default='', max_length=200, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u8d26\u53f7\u4fe1\u606f',
            },
        ),
    ]
