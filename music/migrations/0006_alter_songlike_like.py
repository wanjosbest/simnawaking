# Generated by Django 5.1.4 on 2025-01-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_songlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songlike',
            name='like',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
