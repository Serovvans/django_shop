from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import ProductListView, FeedbackCreateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', FeedbackCreateView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_item')
]
