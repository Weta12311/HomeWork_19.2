# Generated by Django 5.1 on 2024-09-19 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_blog_created_at_blog_image_blog_updated_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="updated_at",
        ),
    ]
