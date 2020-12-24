from django.urls import path

from . import views

urlpatterns = [
  path('api/ping/', views.GetPongView.as_view()),
  path('', views.index, name='index'),
]
