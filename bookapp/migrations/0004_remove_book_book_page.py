# Generated by Django 4.2.1 on 2023-05-21 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_rename_editor_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_page',
        ),
    ]
