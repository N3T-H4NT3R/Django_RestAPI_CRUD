from django.urls import path
from .views import (
    Get_All_Products,
    Get_Each_Product,
    Add_Product,
    Update_Product,
    Delete_Product,
)
urlpatterns = [
    path("products/", Get_All_Products, name="products"),
    path("product/<int:pk>/", Get_Each_Product, name="product"),
    path("product-add/", Add_Product, name="product-add"),
    path("product-update/<int:pk>/", Update_Product, name="product-update"),
    path("product-delete/<int:pk>/", Delete_Product, name="product-delete"),
]
