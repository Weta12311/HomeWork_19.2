from catalog.models import Product
from django.views.generic import TemplateView, DetailView, ListView


class ProductsListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    model = Product
