from django.urls import path
from . import views

urlpatterns = [
    path('cadastrarponto/', views.cadastrarponto, name='cadastrarponto')
]