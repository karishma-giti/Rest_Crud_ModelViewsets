from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Api import views
from Api.views import ProductModelViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'productapi', views.ProductModelViewSet, basename='productapi')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
    
]

