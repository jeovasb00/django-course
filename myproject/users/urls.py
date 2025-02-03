from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.users, name="users"),
    path('register/', views.register_view, name="register"),
]