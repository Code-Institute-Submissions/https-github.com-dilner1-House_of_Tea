# Generated by Django 3.2 on 2022-11-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='order_id',
            field=models.CharField(max_length=32),
        ),
    ]