# Generated by Django 3.0.1 on 2019-12-30 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_why'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='why',
            name='subtitle_why',
        ),
    ]
