from django.urls import path
from . import views

urlpatterns = [
    path('adicionarproduto', views.adicionarproduto, name='adicionarproduto')
]