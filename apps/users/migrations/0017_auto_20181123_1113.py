# Generated by Django 2.1.1 on 2018-11-23 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20181109_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_password_last_updated',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date password last updated'),
        ),
    ]
