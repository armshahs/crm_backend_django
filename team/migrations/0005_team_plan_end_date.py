# Generated by Django 5.0.1 on 2024-02-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_team_stripe_customer_id_team_stripe_subscription_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
