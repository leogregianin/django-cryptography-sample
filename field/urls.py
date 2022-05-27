from rest_framework import routers

from field import viewsets

router = routers.DefaultRouter()

router.register('field', viewsets.FieldViewSet, basename='Field')
router.register('detailfield', viewsets.FieldDetailViewSet, basename='DetailField')

urlpatterns = router.urls
