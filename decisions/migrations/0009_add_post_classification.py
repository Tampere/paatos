# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('decisions', '0008_add_organization_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('data_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='post',
            name='abbreviation',
            field=models.CharField(blank=True, help_text='An abbreviation for the post', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(db_index=True, default='', help_text='Slug for the post', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='action',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='case',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='casegeometry',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='content',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='event',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='eventattendee',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='function',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='importedfile',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='classification',
            field=models.ForeignKey(blank=True, help_text='An organization classification, e.g. committee', null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.OrganizationClass'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='organizationclass',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='person',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.DataSource'),
        ),
        migrations.AddField(
            model_name='post',
            name='classification',
            field=models.ForeignKey(blank=True, help_text='A post classification, e.g. committee', null=True, on_delete=django.db.models.deletion.PROTECT, to='decisions.PostClass'),
        ),
        migrations.AlterUniqueTogether(
            name='postclass',
            unique_together=set([('data_source', 'origin_id')]),
        ),
    ]
