# Generated by Django 3.0.6 on 2020-06-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200626_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='seasons',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='web',
            name='seasons',
            field=models.IntegerField(default='1'),
        ),
    ]
