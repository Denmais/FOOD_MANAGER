# Generated by Django 3.2 on 2023-12-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20231225_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproduct',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]