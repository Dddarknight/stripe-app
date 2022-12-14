# Generated by Django 4.1.3 on 2022-11-18 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0002_order_itemorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stripe_app.discount'),
        ),
    ]
