# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from . import models

from . import serializers

class CreateTodo(generics.ListCreateAPIView):
    queryset = models.TodoModel.objects.all()
    serializer_class = serializers.TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    lookup_field = 'title_id'
    queryset = models.TodoModel.objects.all()
    serializer_class = serializers.TodoSerializer

class UpdateTodo(generics.RetrieveUpdateAPIView):
    lookup_field = 'title_id'
    queryset = models.TodoModel.objects.all()
    serializer_class = serializers.TodoSerializer

class DeleteTodo(generics.DestroyAPIView):
    lookup_field = 'title_id'
    queryset = models.TodoModel.objects.all()
    serializer_class = serializers.TodoSerializer
