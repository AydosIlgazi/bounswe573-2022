# Generated by Django 4.0.3 on 2022-04-24 18:10

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('SweCourseApp', '0004_delete_topic_rename_owner_learningspace_creator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningspace',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]