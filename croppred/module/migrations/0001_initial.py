# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-03-31 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=40)),
                ('dob', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
            ],
        ),
    ]
