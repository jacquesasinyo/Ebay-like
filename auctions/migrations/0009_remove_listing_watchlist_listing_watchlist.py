# Generated by Django 4.1 on 2022-09-11 22:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_remove_listing_watchlist_listing_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
