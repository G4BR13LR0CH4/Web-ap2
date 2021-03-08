from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('del/<int:pk>', views.deletItem, name='del'),
    path('<int:pk>', views.editItem, name='edit'),
]