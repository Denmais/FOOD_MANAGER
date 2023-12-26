# Generated by Django 3.2 on 2023-12-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_userproduct_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='categories/images/'),
        ),
        migrations.AddField(
            model_name='products',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='products/images/'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='subcategories/images/'),
        ),
    ]