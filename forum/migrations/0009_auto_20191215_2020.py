# Generated by Django 3.0 on 2019-12-15 18:20

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20191213_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
