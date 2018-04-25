from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet


router = DefaultRouter()
router.register(r'files', FileViewSet, base_name='file')

urlpatterns = [
    url(r'^', include(router.urls))
]
