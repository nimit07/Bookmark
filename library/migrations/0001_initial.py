# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('author', models.CharField(max_length=80, verbose_name='Author')),
                ('copies', models.IntegerField(verbose_name='Copies')),
            ],
        ),
        migrations.CreateModel(
            name='BooksPerBranch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.CharField(max_length=5, verbose_name='Branch')),
                ('total_books', models.IntegerField(verbose_name='Total_Books')),
            ],
        ),
        migrations.CreateModel(
            name='FieldList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field', models.CharField(max_length=30, verbose_name='Field')),
                ('branch', models.ForeignKey(related_name='branch_name', verbose_name='Branch', to='library.BooksPerBranch')),
            ],
        ),
        migrations.AddField(
            model_name='booklist',
            name='field',
            field=models.ForeignKey(related_name='book_field', verbose_name='Field', to='library.FieldList'),
        ),
    ]
