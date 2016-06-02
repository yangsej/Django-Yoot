# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(default=('빽도', '도', '개', '걸', '윷', '모'), max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=30)),
                ('online', models.BooleanField(default=False)),
                ('mset', models.CharField(default=('빽도', '도', '개', '걸', '윷', '모'), max_length=128)),
                ('combination', models.IntegerField(default=0)),
                ('waiting', models.IntegerField(default=4)),
                ('finish', models.IntegerField(default=0)),
                ('Board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Board')),
            ],
        ),
        migrations.AddField(
            model_name='distance',
            name='Player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Player'),
        ),
    ]
