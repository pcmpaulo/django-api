from rest_framework import viewsets, permissions

from core.users.models import User
from core.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
