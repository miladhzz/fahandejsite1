# Generated by Django 2.2.8 on 2020-01-11 17:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20200110_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='commentarticle',
            name='comment',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='commentgallery',
            name='comment',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='commentproduct',
            name='comment',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='address_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='address_fa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='address_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='full_about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='full_about_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='full_about_fa',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='full_about_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
