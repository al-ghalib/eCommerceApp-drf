from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.product import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('brand', views.BrandViewSet)
router.register('product', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
