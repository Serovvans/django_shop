from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import ProductListView, FeedbackCreateView, ProductDetailView, ProductDeleteView, \
    ProductCreateView, ProductUpdateView, VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', FeedbackCreateView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_item'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('version/create/<int:pk>', VersionCreateView.as_view(), name='version_create')
]
