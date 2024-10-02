from django.urls import path
from .views import IndexPageView, menuView, registro_view, login_view, logout_view, vehiculo_add, vehiculo_list

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path('menu/', menuView, name='menu'),
    path('registro/', registro_view, name="registro"), 
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('vehiculo/add', vehiculo_add, name='vehiculo_add'),
    path('vehiculo/list', vehiculo_list, name='vehiculo_list'),
]