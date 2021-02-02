# Generated by Django 3.1.5 on 2021-01-31 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='image',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='img_alt',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='text',
        ),
        migrations.AddField(
            model_name='vendor',
            name='description',
            field=models.CharField(default='text', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]