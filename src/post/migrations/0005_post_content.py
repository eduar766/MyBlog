# Generated by Django 2.2 on 2019-05-01 16:29

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='Test'),
            preserve_default=False,
        ),
    ]