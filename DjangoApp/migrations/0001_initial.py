# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 22:38
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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('is_publish', models.BooleanField()),
                ('is_denied', models.BooleanField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='banWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('Article_comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoApp.Article')),
            ],
        ),
        migrations.CreateModel(
            name='emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=100)),
                ('Comment_emotion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoApp.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('Article_Tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoApp.Article')),
            ],
        ),
    ]