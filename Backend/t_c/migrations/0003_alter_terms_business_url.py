# Generated by Django 4.0.6 on 2022-08-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_c', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terms',
            name='business_url',
            field=models.URLField(unique=True),
        ),
    ]
