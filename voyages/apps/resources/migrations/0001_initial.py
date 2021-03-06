# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfricanName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slave_id', models.IntegerField(unique=True, verbose_name=b'African id')),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('height', models.FloatField(null=True, verbose_name=b'Height in inches', blank=True)),
                ('source', models.CharField(max_length=30, null=True, verbose_name=b'Modern name', blank=True)),
                ('date_arrived', models.IntegerField(null=True, verbose_name=b'Voyage year', blank=True)),
                ('ship_name', models.CharField(max_length=70, null=True, verbose_name=b'Ship Name', blank=True)),
                ('voyage_number', models.IntegerField(verbose_name=b'Voyage ID')),
            ],
            options={
                'ordering': ['slave_id'],
                'verbose_name': 'African Name',
                'verbose_name_plural': 'African Names',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_id', models.IntegerField(unique=True, verbose_name=b'Country id')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['country_id'],
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=b'images')),
                ('title', models.CharField(default=b'', max_length=200)),
                ('description', models.CharField(default=b'', max_length=2000)),
                ('creator', models.CharField(max_length=200, null=True, blank=True)),
                ('language', models.CharField(max_length=2, null=True, blank=True)),
                ('source', models.CharField(max_length=500, null=True, blank=True)),
                ('ready_to_go', models.BooleanField(default=False)),
                ('order_num', models.IntegerField(null=True, verbose_name=b'Code value', blank=True)),
                ('date', models.IntegerField(null=True, verbose_name=b'Date(Year YYYY)', blank=True)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(verbose_name=b'Code')),
                ('label', models.CharField(max_length=20, verbose_name=b'Category name')),
                ('visible_on_website', models.BooleanField(default=True, verbose_name=b'Visible on website (If checked, category will display on website if there is at least one image to display.)')),
            ],
            options={
                'ordering': ['value'],
                'verbose_name': 'Image Category',
                'verbose_name_plural': 'Image Categories',
            },
        ),
        migrations.CreateModel(
            name='SexAge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sex_age_id', models.IntegerField(unique=True, verbose_name=b'SexAge Id')),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'ordering': ['sex_age_id'],
                'verbose_name': 'Sex Age',
                'verbose_name_plural': 'Sex Ages',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(verbose_name=b'Image category', to='resources.ImageCategory'),
        ),
        migrations.AddField(
            model_name='image',
            name='voyage',
            field=models.ForeignKey(to_field=b'voyage_id', blank=True, to='voyage.Voyage', null=True),
        ),
        migrations.AddField(
            model_name='africanname',
            name='country',
            field=models.ForeignKey(verbose_name=b'Country of Origin', to_field=b'country_id', blank=True, to='resources.Country', null=True),
        ),
        migrations.AddField(
            model_name='africanname',
            name='disembarkation_port',
            field=models.ForeignKey(related_name='disembarkation_port', verbose_name=b'Disembarkation', to_field=b'value', blank=True, to='voyage.Place', null=True),
        ),
        migrations.AddField(
            model_name='africanname',
            name='embarkation_port',
            field=models.ForeignKey(related_name='embarkation_port', verbose_name=b'Embarkation', to_field=b'value', blank=True, to='voyage.Place', null=True),
        ),
        migrations.AddField(
            model_name='africanname',
            name='sex_age',
            field=models.ForeignKey(verbose_name=b'Sex Age', to_field=b'sex_age_id', blank=True, to='resources.SexAge', null=True),
        ),
        migrations.AddField(
            model_name='africanname',
            name='voyage',
            field=models.ForeignKey(verbose_name=b'Voyage', to_field=b'voyage_id', blank=True, to='voyage.Voyage', null=True),
        ),
    ]
