# Generated by Django 3.1.5 on 2021-01-26 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='BlogPost',
        ),
    ]
