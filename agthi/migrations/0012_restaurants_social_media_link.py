# Generated by Django 5.0.8 on 2024-08-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agthi', '0011_latest_news_news_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='social_media_link',
            field=models.URLField(null=True),
        ),
    ]
