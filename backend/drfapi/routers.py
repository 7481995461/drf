from rest_framework.routers import DefaultRouter
from product.viewsets import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet,basename='products')

urlpatterns = router.urls