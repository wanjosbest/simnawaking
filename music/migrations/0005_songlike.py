# Generated by Django 5.1.4 on 2025-01-12 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_newsletter_remove_post_or_paste_song_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='songlike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0, null=True)),
                ('song', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songlike', to='music.post')),
            ],
        ),
    ]