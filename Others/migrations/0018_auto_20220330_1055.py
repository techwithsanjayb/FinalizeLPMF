# Generated by Django 3.2.9 on 2022-03-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Others', '0017_alter_successstories_success_stories_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='successstories',
            old_name='success_stories_images',
            new_name='success_stories_uploadimages',
        ),
        migrations.AddField(
            model_name='successstories',
            name='success_stories_imagelink',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]