# Generated by Django 5.0.1 on 2024-02-27 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leads', to='team.team'),
        ),
    ]
