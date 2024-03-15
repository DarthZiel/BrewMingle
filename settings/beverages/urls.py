from django.urls import path, include
from .views import CoffeeModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'coffee', CoffeeModelViewSet)

urlpatterns = router.urls




