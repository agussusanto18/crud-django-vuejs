# Generated by Django 2.2 on 2021-10-31 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='post'),
        ),
    ]
