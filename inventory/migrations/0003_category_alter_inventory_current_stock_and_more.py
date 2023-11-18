# Generated by Django 4.2.7 on 2023-11-18 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_inventory_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='inventory',
            name='current_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='min_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.category'),
        ),
    ]
