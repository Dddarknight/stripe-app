# Generated by Django 4.1.3 on 2022-11-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0004_tax_alter_order_discount_order_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.TextField(default='usd', max_length=3),
        ),
    ]