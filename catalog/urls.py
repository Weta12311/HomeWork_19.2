from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ProductsListView, ContactsTemplateView, ProductDetailView, ProductUpdateView,
                           ProductCreateView, ProductDeleteView, CategoryListView)
from django.conf import settings


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="index"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product_create", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("category_list/", cache_page(60)(CategoryListView.as_view()), name="category_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
