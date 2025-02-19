from django.urls import include, path
from rest_framework import routers

from core.users.views import UserViewSet

user_router = routers.DefaultRouter()
user_router.register(r'users', UserViewSet)

user_urls = [
    path('', include(user_router.urls)),
]