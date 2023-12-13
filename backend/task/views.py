from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import AllowAny


class TaskListCreatAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()



class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)