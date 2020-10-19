from django.shortcuts import render
from rest_framework import viewsets
from center.events.models import User
from center.events.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
