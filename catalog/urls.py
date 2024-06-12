from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.views import (home, contacts, ProductsCreateView,
                           ProductsUpdateView, ProductsListView,
                           ProductView, ProductDeleteView, CategoryListView)

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products_list/', ProductsListView.as_view(), name='products_list'),
    path('create/', ProductsCreateView.as_view(), name='create'),
    path('products_list/<int:pk>/', cache_page(60)(ProductView.as_view()), name='view'),
    path('edit/<int:pk>/', ProductsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
]
