# Generated by Django 2.2 on 2019-04-27 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='catgory',
            new_name='category',
        ),
    ]
