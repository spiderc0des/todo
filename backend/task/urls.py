from django.urls import path, include
from task import views

from rest_framework import routers

# router = routers.DefaultRouter()

# router.register(r'tasks', TaskViewSet)
# router.registe

urlpatterns = [
    path('', views.TaskListCreatAPIView.as_view()),
    path('<int:pk>/update/', views.TaskUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.TaskDestroyAPIView.as_view())

]