from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Blog
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.urls import reverse_lazy


class ProductsListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    model = Product

