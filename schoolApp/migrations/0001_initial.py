# Generated by Django 4.2.17 on 2025-03-10 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_number', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('index_number', 'province', 'district')},
            },
        ),
    ]
