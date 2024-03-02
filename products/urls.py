from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name="home"),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]
