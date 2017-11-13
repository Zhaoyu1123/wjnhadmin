# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import (
    ProductList,
    ProductDetail,
    ProductUpdate,
    ProductCreate,
)


urlpatterns = [
    url(r'^list/$', ProductList.as_view()),
    url(r'^(?P<pk>[0-9]+)/detail/$', ProductDetail.as_view(), name='product_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', ProductUpdate.as_view(), name='product_update'),

    url(r'^create/$', ProductCreate.as_view(), name='product_create'),
]
