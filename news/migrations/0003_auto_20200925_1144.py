# Generated by Django 3.1.1 on 2020-09-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish_date',
            field=models.DateField(auto_now=True),
        ),
    ]
