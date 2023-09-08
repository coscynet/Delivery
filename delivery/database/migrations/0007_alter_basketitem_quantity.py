# Generated by Django 4.2.4 on 2023-09-08 10:19

import database.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_alter_item_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='quantity',
            field=models.IntegerField(default=1, validators=[database.validators.quantity_validator]),
        ),
    ]
