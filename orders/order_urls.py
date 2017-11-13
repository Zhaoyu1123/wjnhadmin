# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import (
    OrderList,
    OrderDetail,
    OrderCreate,
    OrderUpdate,
)


urlpatterns = [
    url(r'^list/$', OrderList.as_view(), name='order_list'),
    url(r'^(?P<pk>[0-9]+)/detail/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', OrderUpdate.as_view(), name='order_update'),

    url(r'^create/$', OrderCreate.as_view(), name='order_create'),
]
