# Generated by Django 4.2.4 on 2023-09-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_review_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='taken_in_calculation',
            field=models.BooleanField(default=True),
        ),
    ]
