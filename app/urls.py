# from sample.app.views import ProductDetailView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:pk>", views.ProductDetailView.as_view(), name="product-detail"),
]
