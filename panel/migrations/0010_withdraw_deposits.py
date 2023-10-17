# Generated by Django 4.2.5 on 2023-10-10 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel', '0009_alter_affiliate_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='withdraw',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('in_progress', 'In Progress')], default='pending', max_length=20)),
                ('withdraw_created_at', models.DateTimeField(auto_now_add=True)),
                ('withdraw_updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'withdraw',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='deposits',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('in_progress', 'In Progress')], default='pending', max_length=20)),
                ('deposits_created_at', models.DateTimeField(auto_now_add=True)),
                ('deposits_updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'deposits',
                'managed': True,
            },
        ),
    ]
