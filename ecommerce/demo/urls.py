from django.urls import path
from ecommerce.demo import views

app_name = "demo"

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.category, name="category"),
    path(
        "product-by-category/<slug:category>/",  # <datatype:value>
        views.product_by_category,
        name="product_by_category",
    ),
    path(
        "<slug:slug>/",
        views.product_detail,
        name="product_detail",
    ),
]
