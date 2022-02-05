from django.shortcuts import render
from django.views.generic.detail import DetailView
from store.models import Product

# Create your views here.


def home(request):

    products = Product.objects.all().filter(is_available=True)

    context = {"products": products}

    return render(request, "app/home.html", context)


class ProductDetailView(DetailView):
    model = Product
