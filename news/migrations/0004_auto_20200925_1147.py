# Generated by Django 3.1.1 on 2020-09-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200925_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
