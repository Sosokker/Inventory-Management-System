# Generated by Django 4.2.7 on 2023-11-18 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_item_previous_inventory_alter_item_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='previous_inventory',
        ),
    ]