# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-30 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=200, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('isDone', models.BooleanField()),
                ('doneAt', models.DateTimeField(blank=True)),
            ],
        ),
    ]
