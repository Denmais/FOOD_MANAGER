from rest_framework import routers 
from django.contrib import admin 
from django.urls import include, path
from api.views import CategoryViewSet, SubCategoryViewSet, ProductViewSet, BagView
 
 
router_v1 = routers.DefaultRouter() 
router_v1.register(r'categories', CategoryViewSet, basename='categories') 
router_v1.register(r'categories/(?P<category_slug>[-\w]+)/subcategories', SubCategoryViewSet, 
                basename='subcategories') 
router_v1.register(r'categories/(?P<category_slug>[-\w]+)/subcategories/(?P<subcategory_slug>[-\w]+)/products', ProductViewSet)




urlpatterns = [
#    path('v1/auth/', include(auth_patern)),
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')), 
    path('v1/', include('djoser.urls.jwt')),
    path('v1/me/', BagView.as_view())
]
