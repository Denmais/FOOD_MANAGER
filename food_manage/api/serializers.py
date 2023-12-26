from rest_framework import serializers
from django.db.models import Sum
from api.models import Category, SubCategory, Products, UserProduct


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор запроса на категории"""

    class Meta:
        model = Category
        exclude = ('id', 'slug')


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор запроса на подкатегории"""
    category = serializers.StringRelatedField()

    class Meta:
        model = SubCategory
        exclude = ('id', 'slug')


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор запроса на продукты"""
    subcategory = serializers.StringRelatedField()
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.subcategory.category.name

    class Meta:
        model = Products
        exclude = ('id', 'slug')


class UserTakeProductSerializer(serializers.ModelSerializer):
    """Сериализатор запроса на добавление продукта в корзину"""
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProduct
        exclude = ('id', 'user',)
        read_only_fields = ('owner', 'price')


class UserListProductSerializer(serializers.Serializer):
    """Сериализатор запроса на просмотр корзины."""
    product_count = serializers.SerializerMethodField()  # Счетчик кол-ва продуктов
    list_products = serializers.SerializerMethodField()  # Список продуктов
    price = serializers.SerializerMethodField()  # Общая цена корзины

    def get_product_count(self, obj):
        return obj.aggregate(Sum('count'))['count__sum']

    def get_list_products(self, obj):
        return UserTakeProductSerializer(obj, many=True).data

    def get_price(self, obj):
        final_price = 0
        for prod_price in obj:
            final_price += prod_price.price*prod_price.count
        return final_price
