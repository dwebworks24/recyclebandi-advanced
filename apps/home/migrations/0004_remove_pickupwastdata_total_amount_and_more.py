# Generated by Django 5.0.6 on 2024-06-26 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_pointes_pickupwastdata_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickupwastdata',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='pickuptransaction',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
