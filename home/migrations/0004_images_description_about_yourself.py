# Generated by Django 2.1.2 on 2019-01-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190129_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='description_about_yourself',
            field=models.TextField(default='Describe in Brief'),
        ),
    ]