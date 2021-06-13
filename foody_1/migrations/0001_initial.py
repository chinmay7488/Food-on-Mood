# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-06 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoodData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dish', models.CharField(max_length=50)),
                ('happie', models.IntegerField()),
                ('angrie', models.IntegerField()),
                ('dehydratie', models.IntegerField()),
                ('depressie', models.IntegerField()),
                ('excitie', models.IntegerField()),
                ('unwellie', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=6)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cost', models.IntegerField()),
                ('count', models.IntegerField()),
                ('chholebature', models.IntegerField()),
                ('rajmachawal', models.IntegerField()),
                ('dosa', models.IntegerField()),
                ('idli', models.IntegerField()),
                ('noodles', models.IntegerField()),
                ('chillypaneer', models.IntegerField()),
                ('alootikki', models.IntegerField()),
                ('vadapao', models.IntegerField()),
                ('garlicbread', models.IntegerField()),
                ('pasta', models.IntegerField()),
                ('springroll', models.IntegerField()),
                ('ham', models.IntegerField()),
                ('icecream', models.IntegerField()),
                ('pastries', models.IntegerField()),
                ('chocolates', models.IntegerField()),
                ('tea', models.IntegerField()),
                ('softdrinks', models.IntegerField()),
                ('juices', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=6)),
                ('distance', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('yesno', models.IntegerField()),
            ],
        ),
    ]
