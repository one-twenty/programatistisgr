# Generated by Django 3.0 on 2019-12-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_category_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
