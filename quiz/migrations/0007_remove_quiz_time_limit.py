# Generated by Django 2.2.6 on 2020-04-25 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_quiz_time_limit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='time_limit',
        ),
    ]
