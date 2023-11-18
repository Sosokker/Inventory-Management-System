# Generated by Django 4.2.7 on 2023-11-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_alter_supply_options_alter_order_order_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='from_date_timestamp',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='to_date_timestamp',
        ),
        migrations.AddField(
            model_name='transfer',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]