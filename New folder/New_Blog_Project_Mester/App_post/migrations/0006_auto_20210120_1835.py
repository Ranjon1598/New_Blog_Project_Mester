# Generated by Django 3.1.4 on 2021-01-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_post', '0005_auto_20210120_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publich_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]