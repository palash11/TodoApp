# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from users.models import User
from rest_framework import generics

from users.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().filter(username=self.request.user)
