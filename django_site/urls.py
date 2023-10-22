# django_site/urls.py
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("chat/", include("chat.urls")),
    path('login/', views.user_login, name='user_login'),
]
