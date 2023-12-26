from django.db import models
from django.contrib.auth.models import AbstractUser


MAX_LENGTH = 100


class Category(models.Model):
    """Класс категории."""
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH
    )
    slug = models.CharField(
        verbose_name='Slug',
        max_length=MAX_LENGTH
    )
    photo = models.ImageField(
        upload_to='categories/images/',
        null=True,
        verbose_name='Фото',
        default=None,
        blank=True
        )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """Класс подкатегории."""
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH
    )
    slug = models.CharField(
        verbose_name='Slug',
        max_length=MAX_LENGTH
    )
    photo = models.ImageField(
        upload_to='subcategories/images/',
        null=True,
        verbose_name='Фото',
        default=None,
        blank=True
        )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='subcategory',
        null=True
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Products(models.Model):
    """Класс продукта."""
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH
    )
    slug = models.CharField(
        verbose_name='Slug',
        max_length=MAX_LENGTH
    )
    photo = models.ImageField(
        upload_to='products/images/',
        null=True,
        verbose_name='Фото',
        default=None,
        blank=True
        )
    subcategory = models.ForeignKey(
        SubCategory,
        verbose_name='Подкатегория',
        on_delete=models.SET_NULL,
        related_name='products',
        null=True
    )
    price = models.IntegerField(verbose_name='Цена 1шт',)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'
        ordering = ('name',)

    def __str__(self):
        return self.name


class UserModel(AbstractUser):
    bag = models.ManyToManyField(Products, through='UserProduct')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)


class UserProduct(models.Model):
    """Класс корзины."""
    user = models.ForeignKey(
        UserModel,
        verbose_name='Пользователь',
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        Products,
        verbose_name='Продукт',
        on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Пользователь и продукт'
        verbose_name_plural = 'Пользователи и продукты'
