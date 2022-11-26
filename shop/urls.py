from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.ShopViewSet, basename='shop')

urlpatterns = router.urls
