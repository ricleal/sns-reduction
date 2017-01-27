# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 17:46
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import server.apps.sans.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        ('django_remote_submission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BioSANSConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('wavelength', models.DecimalField(blank=True, decimal_places=2, help_text='If empty uses the value set in the data file.', max_digits=4, null=True, verbose_name='Wavelength (Å)')),
                ('wavelength_spread', models.DecimalField(blank=True, decimal_places=2, help_text='If empty uses the value set in the data file.', max_digits=3, null=True, verbose_name='Wavelength Spread (%)')),
                ('sample_detector_distance', models.DecimalField(blank=True, decimal_places=3, help_text='(in meters) If empty uses the value set in the data file.', max_digits=5, null=True, verbose_name='Sample Detector Distance (m)')),
                ('solid_angle_correction', models.CharField(blank=True, choices=[('', 'None'), ('detector_tubes=False, detector_wing=False', 'Regular'), ('detector_tubes=Tubes, detector_wing=False', 'Tubes'), ('detector_tubes=False, detector_wing=True', 'Wing')], default='', max_length=50, null=True)),
                ('absolute_scale_factor', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('sample_aperture_diameter', models.DecimalField(decimal_places=2, default=10.0, max_digits=10)),
                ('direct_beam_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('mask_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('dark_current_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('sensitivity_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('sensitivity_min', models.DecimalField(decimal_places=2, default=0.4, max_digits=10)),
                ('sensitivity_max', models.DecimalField(decimal_places=2, default=2.0, max_digits=10)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='BioSANSReduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('ipts', models.CharField(max_length=16)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('script', models.TextField(blank=True, help_text='Python script generated from the reduction entry.')),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='BioSANSRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('comments', models.CharField(blank=True, help_text='Any necessary comments...', max_length=256)),
                ('entries', django.contrib.postgres.fields.jsonb.JSONField(default=[[None, None, None, None, None, None]])),
                ('empty_beam', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='GPSANSConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('wavelength', models.DecimalField(blank=True, decimal_places=2, help_text='If empty uses the value set in the data file.', max_digits=4, null=True, verbose_name='Wavelength (Å)')),
                ('wavelength_spread', models.DecimalField(blank=True, decimal_places=2, help_text='If empty uses the value set in the data file.', max_digits=3, null=True, verbose_name='Wavelength Spread (%)')),
                ('sample_detector_distance', models.DecimalField(blank=True, decimal_places=3, help_text='(in meters) If empty uses the value set in the data file.', max_digits=5, null=True, verbose_name='Sample Detector Distance (m)')),
                ('solid_angle_correction', models.CharField(blank=True, choices=[('', 'None'), ('detector_tubes=False, detector_wing=False', 'Regular'), ('detector_tubes=Tubes, detector_wing=False', 'Tubes')], default='', max_length=50)),
                ('absolute_scale_factor', models.DecimalField(decimal_places=2, default=1.0, max_digits=3)),
                ('normalization', models.CharField(choices=[('NoNormalization()', 'None'), ('TimeNormalization()', 'Time'), ('MonitorNormalization()', 'Monitor')], default='MonitorNormalization()', max_length=50)),
                ('dark_current_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('sample_aperture_diameter', models.DecimalField(decimal_places=2, default=10.0, max_digits=10)),
                ('direct_beam_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('mask_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('sensitivity_file', models.CharField(blank=True, help_text='File path', max_length=256)),
                ('sensitivity_min', models.DecimalField(decimal_places=2, default=0.4, max_digits=10)),
                ('sensitivity_max', models.DecimalField(decimal_places=2, default=2.0, max_digits=10)),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='GPSANSReduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('ipts', models.CharField(max_length=16)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('script', models.TextField(blank=True, help_text='Python script generated from the reduction entry.')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gpsansreduction_instruments', related_query_name='gpsansreduction_instrument', to='catalog.Instrument')),
                ('script_interpreter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gpsansreduction_interpreters', related_query_name='gpsansreduction_interpreter', to='django_remote_submission.Interpreter')),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
        migrations.CreateModel(
            name='GPSANSRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('comments', models.CharField(blank=True, help_text='Any necessary comments...', max_length=256)),
                ('entries', django.contrib.postgres.fields.jsonb.JSONField(default=[[None, None, None, None, None, None]])),
                ('empty_beam', models.CharField(max_length=256)),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='sans.GPSANSConfiguration')),
                ('reduction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', related_query_name='region', to='sans.GPSANSReduction')),
            ],
            options={
                'abstract': False,
                'ordering': ['id'],
            },
            bases=(models.Model, server.apps.sans.models.ModelMixin),
        ),
    ]
