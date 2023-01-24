from django.urls import path, include
from api import views

urlpatterns = [
    path('products/<int:id>/', views.product_id),
    path('products/', views.products),
    path('categories/<int:id>/', views.category_id),
    path('categories/', views.categories),
]
