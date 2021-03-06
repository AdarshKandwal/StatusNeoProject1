# Generated by Django 3.1.6 on 2021-02-24 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='bookname',
        ),
        migrations.AddField(
            model_name='article',
            name='avalaible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
