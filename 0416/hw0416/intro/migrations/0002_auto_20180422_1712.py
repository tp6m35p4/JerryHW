# Generated by Django 2.0.3 on 2018-04-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='birthday',
            field=models.DateField(),
        ),
    ]
