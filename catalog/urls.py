from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (ProductsListView, ContactsTemplateView, ProductDetailView, ProductUpdateView,
                           ProductCreateView, ProductDeleteView)
from django.conf import settings


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="index"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_create", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
