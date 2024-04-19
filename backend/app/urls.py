from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'deadline', DealineView)
# r mostra que não é uma simples String, ele vai funcionar como um ponteiro de memória.

urlpatterns = router.urls
