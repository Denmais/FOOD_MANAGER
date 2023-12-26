# Generated by Django 3.2 on 2023-12-26 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20231226_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='categories/images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='products/images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='Цена 1шт'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategory', to='api.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='subcategories/images/', verbose_name='Фото'),
        ),
    ]
