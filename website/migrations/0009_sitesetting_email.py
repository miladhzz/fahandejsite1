# Generated by Django 2.2.8 on 2020-01-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_sitesetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
