# Generated by Django 4.2.5 on 2023-10-16 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0022_deposits_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposits',
            name='qr_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
