# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-02 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tumblr', '0003_audio_chat_image_link_quote_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='name',
        ),
    ]