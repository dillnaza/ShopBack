from django.urls import path, include
from api import views

urlpatterns = [
    path('products/<int:id>/', views.product_id),
    path('products/', views.products),
    path('categories/<int:pk>/', views.CategoryIDView.as_view({'get': 'retrieve'})),
    path('categories/', views.CategoryView.as_view({'get': 'list'})),
]
