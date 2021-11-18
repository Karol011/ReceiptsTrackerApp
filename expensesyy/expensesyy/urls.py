"""expensesyy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products.views import base_view, product_view, get_custom_product_view, product_create_view, product_update_view, product_delete_view, receipt_view, receipt_create_view, receipt_update_view, receipt_delete_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_view, name="main"),
    path('products/', product_view, name="products"),
    path('products/<int:pk>', get_custom_product_view),
    path('products/create', product_create_view, name="products-create"),
    path('products/update/<int:pk>', product_update_view, name="products-update"),
    path('products/delete/<int:pk>', product_delete_view, name="products-delete"),

    path('receipts/', receipt_view, name="receipts"),
    path('receipts/create', receipt_create_view, name="receipts-create"),
    path('receipts/update/<int:pk>', receipt_update_view, name="receipts-update"),
    path('receipts/delete/<int:pk>', receipt_delete_view, name="receipts-delete"),


]
