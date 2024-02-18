from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
