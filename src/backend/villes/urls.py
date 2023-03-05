"""
Villes urls
"""
from django.conf.urls import url, include
from rest_framework_nested import routers

from villes.views import VillesViewSet


ROUTER = routers.SimpleRouter()
ROUTER.register(r"villes", VillesViewSet, base_name="villes")

urlpatterns = [
    url(r"^", include(ROUTER.urls)),
]
