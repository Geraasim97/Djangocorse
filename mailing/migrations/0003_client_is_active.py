# Generated by Django 4.2.5 on 2023-10-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_client_owner_mailing_owner_message_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
    ]