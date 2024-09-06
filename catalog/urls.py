from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts
from django.conf import settings


app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="index"),
    path("contacts/", contacts, name="contacts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
