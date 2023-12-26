from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Category, SubCategory, Products, UserProduct
from api.serializers import (CategorySerializer, SubcategorySerializer,
                             ProductSerializer, UserTakeProductSerializer, UserListProductSerializer)
from api.permissions import ReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет категории."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
    http_method_names = ["get"]


class SubCategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет подкатегории."""
    queryset = SubCategory.objects.all()
    serializer_class = SubcategorySerializer
    lookup_field = "slug"
    http_method_names = ["get"]

    def get_queryset(self):
        comment = SubCategory.objects.filter(category_id=Category.objects.get(
            slug=self.kwargs.get("category_slug")).id)
        return comment


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет продукта"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [ReadOnly]

    def get_queryset(self):
        queryset = Products.objects.filter(subcategory_id=SubCategory.objects.
                                           get(slug=self.kwargs.get(
                                               "subcategory_slug")).id)
        return queryset

    @action(methods=['post', 'patch', 'delete'], detail=True,
            permission_classes=[permissions.IsAuthenticated])
    def take(self, request, category_slug, subcategory_slug, slug):
        """Функция добавления продукта."""
        user = request.user
        product = Products.objects.get(slug=slug)
        price = Products.objects.get(slug=slug).price
        if request.method == "POST":
            if UserProduct.objects.filter(user=user, product=product).exists():
                bag = UserProduct.objects.get(user=user, product=product)
                old_count = bag.count
                new_count = old_count + request.data["count"]
                request.data["count"] = new_count
                serializer = UserTakeProductSerializer(bag, data=request.data)
            else:
                serializer = UserTakeProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user, product=product, price=price)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == "PATCH":
            bag = UserProduct.objects.get(user=user, product=product)
            serializer = UserTakeProductSerializer(bag, data=request.data,
                                                   partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        bag = UserProduct.objects.get(user=user, product=product)
        bag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BagView(APIView):
    """Класс корзины."""
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        products = UserProduct.objects.filter(user=request.user)
        serializer = UserListProductSerializer(products)
        return Response(serializer.data)

    def delete(self, request):
        products = UserProduct.objects.filter(user=request.user)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
