# Generated by Django 4.0.6 on 2022-08-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=200, null=True)),
                ('business_url', models.URLField()),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('marketing_services', models.CharField(blank=True, max_length=300, null=True)),
                ('tracking_services', models.CharField(blank=True, max_length=300, null=True)),
                ('captcha_service', models.CharField(blank=True, max_length=300, null=True)),
                ('adapt_to_ccpa', models.BooleanField()),
                ('adapt_to_gdpr', models.BooleanField()),
                ('adapt_to_calopa', models.BooleanField()),
                ('contact_info', models.EmailField(blank=True, max_length=254, null=True)),
                ('permanent', models.BooleanField(blank=True, null=True)),
                ('create_date', models.DateTimeField()),
                ('last_edit', models.DateTimeField()),
            ],
            options={
                'ordering': ['last_edit'],
            },
        ),
    ]
