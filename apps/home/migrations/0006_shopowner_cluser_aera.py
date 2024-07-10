# Generated by Django 5.0.6 on 2024-06-28 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_clusteraera'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopowner',
            name='cluser_aera',
            field=models.ForeignKey(db_column='cluster_aera', default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cluster', to='home.clusteraera'),
        ),
    ]
