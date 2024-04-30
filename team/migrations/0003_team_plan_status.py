# Generated by Django 5.0.1 on 2024-02-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_plan_team_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_status',
            field=models.CharField(choices=[('PLAN_ACTIVE', 'Active'), ('PLAN_CANCELLED', 'Cancelled')], default='active', max_length=20),
        ),
    ]
