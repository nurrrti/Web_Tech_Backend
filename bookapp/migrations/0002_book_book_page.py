# Generated by Django 4.2.1 on 2023-05-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_page',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
