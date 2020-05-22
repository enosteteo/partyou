"""ccprod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from ccprod.store import views

urlpatterns = [
    path('store/', views.store_list),
    # path('store/create', views.create_orders),
    # path('store/view/<id::int>'),
    # path('store/admin/create/', views.create_product),
    # path('store/admin/list/', views.list_all_orders),
    # path('store/admin/list/edit', views.edit_orders),
]
