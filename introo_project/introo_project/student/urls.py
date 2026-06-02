from django.urls import path
from . import views
from .views import greet, get_name, user_data, greet_to_user

urlpatterns = [
    path('', views.home, name='home'),
    path('message', greet),
    path('name', get_name),
    path('data', user_data),
    path('user_message/<str:name>/<int:age>', greet_to_user),
]