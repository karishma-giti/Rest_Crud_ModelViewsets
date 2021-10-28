from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Api import views
from Api.views import ProductModelViewSet
from Api.views import UserViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'productapi', views.ProductModelViewSet, basename='productapi')
router.register(r'product', views.UserViewSet, basename='product')
router.register(r'productmixin', views.ProductViewSet, basename='productmixin')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ap/',include(router.urls))
    
]

