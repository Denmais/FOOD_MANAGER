# Generated by Django 3.2 on 2023-12-26 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20231226_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategory', to='api.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='subcategories/images/', verbose_name='Фото'),
        ),
    ]
