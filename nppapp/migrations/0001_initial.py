# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='postindtable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('officename', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('officeType', models.CharField(max_length=100)),
                ('Deliverystatus', models.CharField(max_length=100)),
                ('divisionname', models.CharField(max_length=100)),
                ('regionname', models.CharField(max_length=100)),
                ('circlename', models.CharField(max_length=100)),
                ('taluk', models.CharField(max_length=100)),
                ('Districtname', models.CharField(max_length=100)),
                ('statename', models.CharField(max_length=100)),
            ],
        ),
    ]
