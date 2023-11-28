from django.urls import path, re_path
# from hello import views
from . import views

urlpatterns = [
    path('index', views.index),
    re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    re_path(r'^user/(?P<name>\D+)', views.user),
    re_path(r'user', views.user),
    path('error', views.ERROR)
]
