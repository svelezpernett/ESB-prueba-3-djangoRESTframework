from django.urls import path, include
from rest_framework import routers
from ESB_api.views import *

router_api = routers.DefaultRouter()
router_api.register(r'clientes', Cliente_viewset)