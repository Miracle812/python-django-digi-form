# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-13 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('contacts', '0003_auto_20161013_1720'),
        ('form_document', '0003_auto_20160920_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentSignature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('object_id', models.PositiveIntegerField()),
                ('is_witnessed', models.BooleanField(default=False)),
                ('require_witness', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('signer_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signers', to='contacts.Person')),
                ('witness_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='witnesses', to='contacts.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='formdocumentlink',
            name='access_code',
        ),
        migrations.RemoveField(
            model_name='formdocumentlink',
            name='email',
        ),
        migrations.RemoveField(
            model_name='formdocumentlink',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='formdocumentlink',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='formdocumentlink',
            name='phone',
        ),
    ]
