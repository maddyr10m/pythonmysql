from django.urls import path
from .views import home, UpdateExp, reports, addData, addDetailData

urlpatterns = [
    path('', home, name='home'),
    path('UpdateExp/', UpdateExp, name='UpdateExp'),
    path('Reports/', reports, name='reports'),
    path('addDetailData/', addDetailData, name='addDetailData'),
    path('addData/', addData, name='addData'),
]

