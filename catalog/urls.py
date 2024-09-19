from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ContactsTemplateView, ProductDetailView
from django.conf import settings


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="index"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
