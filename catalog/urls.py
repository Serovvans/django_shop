from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import home, contacts, item

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', item, name='product_item')
]
