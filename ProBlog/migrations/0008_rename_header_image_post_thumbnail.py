# Generated by Django 4.1.2 on 2022-12-04 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ProBlog", "0007_post_header_image_alter_post_snippet"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post", old_name="header_image", new_name="thumbnail",
        ),
    ]
