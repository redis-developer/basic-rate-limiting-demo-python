from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
  path('api/ping/', views.GetPongView.as_view()),
  path('', views.index, name='index'),
  re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
]
