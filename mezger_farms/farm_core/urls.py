from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import FarmViewSet

router = DefaultRouter(trailing_slash=False)
router.register('farms',FarmViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls))

]