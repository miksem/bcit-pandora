# Generated by Django 3.1.5 on 2021-01-31 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_alt', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
            ],
        ),
    ]
