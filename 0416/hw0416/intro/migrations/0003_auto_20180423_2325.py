# Generated by Django 2.0.3 on 2018-04-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0002_auto_20180422_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='department',
            field=models.CharField(default='NTUST', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='people',
            name='university',
            field=models.CharField(default='NTUST', max_length=100),
            preserve_default=False,
        ),
    ]
