from django.urls import path
from diary import views

urlpatterns = [
    path('', views.mem_index),
    path('<int:pk>/', views.mem_detail),
    path('new/', views.mem_new),
]