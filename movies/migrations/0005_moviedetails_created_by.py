# Generated by Django 5.0.6 on 2024-06-26 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_category_alter_moviedetails_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetails',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.profile'),
        ),
    ]
