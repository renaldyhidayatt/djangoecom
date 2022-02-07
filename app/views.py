from django.shortcuts import render
from django.views.generic.detail import DetailView
from store.models import Product, ReviewRating, ProductGalary
from orders.models import OrderProduct


def home(request):

    products = Product.objects.all().filter(is_available=True)

    context = {"products": products}

    return render(request, "app/home.html", context)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, product_id=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["reviews"] = ReviewRating.objects.filter(
            product_id=self.object.id, status=True
        )
        context["product_galary"] = ProductGalary.objects.filter(
            product_id=self.object.id
        )

        if self.request.user.is_authenticated:
            try:
                context["orderproduct"] = OrderProduct.objects.filter(
                    user=self.request.user, product_id=self.object.id
                ).exists()
            except OrderProduct.DoesNotExist:
                orderproduct = None
        else:
            orderproduct = None

        return context
