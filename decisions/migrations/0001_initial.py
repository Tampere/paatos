# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 12:29
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('title', models.CharField(help_text='Title of the action', max_length=255)),
                ('ordering', models.IntegerField(help_text='Ordering of this action within a meeting')),
                ('article_number', models.CharField(blank=True, help_text='The article number given to this action after decision', max_length=255)),
                ('resolution', models.CharField(blank=True, help_text='Resolution taken in this action (like tabled, decided...)', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, help_text='Short name of this attachment', max_length=400)),
                ('url', models.URLField(help_text='URL of the content of this attachment')),
                ('number', models.PositiveIntegerField(help_text='Index number of this attachment')),
                ('public', models.BooleanField(default=False, help_text='Is this attachment public?')),
                ('confidentiality_reason', models.CharField(blank=True, help_text='Reason for keeping this attachment confidential', max_length=100)),
                ('action', models.ForeignKey(help_text='The action this attachment is related to', on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='decisions.Action')),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('title', models.CharField(help_text='Descriptive compact title for this case', max_length=255)),
                ('register_id', models.CharField(db_index=True, help_text='Register ID of this case', max_length=255, unique=True)),
                ('attachments', models.ManyToManyField(related_name='cases', to='decisions.Attachment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CaseGeometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('type', models.CharField(choices=[('address', 'Address'), ('plan', 'Plan'), ('district', 'District')], db_index=True, max_length=20)),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('ordering', models.IntegerField(help_text='Ordering of this content within the larger context (like action)')),
                ('title', models.CharField(blank=True, help_text='Title of this content', max_length=255)),
                ('type', models.CharField(help_text='Type of this content (options include: decision, proposal, proceedings...)', max_length=255)),
                ('hypertext', models.TextField(help_text='Content formatted with pseudo-HTML. Only a very restricted set of tags is allowed. These are: first and second level headings (P+H1+H2) and table (more may be added, but start from a minimal set)')),
                ('action', models.ForeignKey(help_text='Action that this content describes', on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='decisions.Action')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('identifier', models.CharField(db_index=True, max_length=255, unique=True)),
                ('name', models.CharField(help_text='Human-readable name', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, help_text="The event's name", max_length=255)),
                ('start_date', models.DateField(help_text='The time at which the event starts')),
                ('end_date', models.DateField(blank=True, help_text='The time at which the event ends', null=True)),
                ('data_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('name', models.CharField(help_text='Name of this function', max_length=255)),
                ('function_id', models.CharField(help_text='Original identifier of this function', max_length=32)),
                ('data_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource')),
                ('parent', models.ForeignKey(blank=True, help_text='Parent function of this function', null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.Function')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, help_text='The role that the person fulfills in the organization', max_length=255, null=True)),
                ('start_date', models.DateField(blank=True, help_text='The date on which the relationship began', null=True)),
                ('end_date', models.DateField(blank=True, help_text='The date on which the relationship ended', null=True)),
                ('data_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('classification', models.CharField(help_text='An organization category, e.g. committee', max_length=255)),
                ('name', models.CharField(help_text='A primary name, e.g. a legally recognized name', max_length=255)),
                ('founding_date', models.DateField(blank=True, help_text='A date of founding', null=True)),
                ('dissolution_date', models.DateField(blank=True, help_text='A date of dissolution', null=True)),
                ('data_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource')),
                ('parent', models.ForeignKey(blank=True, help_text='The organizations that contain this organization', null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('name', models.CharField(help_text="A person's preferred full name", max_length=255)),
                ('given_name', models.CharField(help_text='One or more primary given names', max_length=255)),
                ('family_name', models.CharField(help_text='One or more family names', max_length=255)),
                ('data_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which the resource was created')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The time at which the resource was updated')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('label', models.CharField(help_text='A label describing the post', max_length=255)),
                ('start_date', models.DateField(blank=True, help_text='The date on which the post was created', null=True)),
                ('end_date', models.DateField(blank=True, help_text='The date on which the post was eliminated', null=True)),
                ('data_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource')),
                ('organization', models.ForeignKey(help_text='The organization in which the post is held', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='decisions.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(help_text='The organization in which the person or organization is a member', on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='decisions.Organization'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(help_text='Person who has membership in organization', on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='decisions.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(blank=True, help_text='The organization organizing the event', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='decisions.Organization'),
        ),
        migrations.AddField(
            model_name='content',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource'),
        ),
        migrations.AddField(
            model_name='casegeometry',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource'),
        ),
        migrations.AddField(
            model_name='case',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource'),
        ),
        migrations.AddField(
            model_name='case',
            name='function',
            field=models.ForeignKey(help_text='Function this case belongs to ("tehtäväluokka")', on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='decisions.Function'),
        ),
        migrations.AddField(
            model_name='case',
            name='geometries',
            field=models.ManyToManyField(blank=True, help_text='Geometries related to this case', related_name='cases', to='decisions.CaseGeometry'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource'),
        ),
        migrations.AddField(
            model_name='action',
            name='case',
            field=models.ForeignKey(blank=True, help_text='Case this action is related to', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='decisions.Case'),
        ),
        migrations.AddField(
            model_name='action',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decisions.DataSource'),
        ),
        migrations.AddField(
            model_name='action',
            name='event',
            field=models.ForeignKey(blank=True, help_text='Event this action is related to', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='decisions.Event'),
        ),
        migrations.AddField(
            model_name='action',
            name='post',
            field=models.ForeignKey(blank=True, help_text='If this decision was delegated, this field will be filled and refers to the post that made the decision', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='decisions.Post'),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='organization',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='function',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='casegeometry',
            unique_together=set([('name', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='case',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='action',
            unique_together=set([('data_source', 'origin_id')]),
        ),
    ]
