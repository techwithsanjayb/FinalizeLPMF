# Generated by Django 3.2.9 on 2022-03-30 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Others', '0018_auto_20220330_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstories',
            name='success_stories_category',
            field=models.CharField(choices=[('Startup Deployment', 'Startup Deployment'), ('Localisation Deployment', 'Localisation Deployment'), ('Proof of concept/Demo', 'Proof of concept/Demo'), ('Services Deployment', 'Services Deployment'), ('AP Success Stories', 'AP Success Stories'), ('Advanced Features', 'Advanced Features'), ('Archive', 'Archive')], default='', max_length=50),
        ),
    ]
