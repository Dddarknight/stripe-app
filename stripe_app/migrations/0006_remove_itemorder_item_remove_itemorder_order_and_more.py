# Generated by Django 4.1.3 on 2022-11-18 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0005_item_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemorder',
            name='item',
        ),
        migrations.RemoveField(
            model_name='itemorder',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ItemOrder',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Tax',
        ),
    ]
