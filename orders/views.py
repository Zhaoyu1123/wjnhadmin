# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.http import urlencode
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from models import Product, POrder
from forms import OrderForm, ProductForm


class ProductList(ListView):
    model = Product
    paginate_by = 12
    context_object_name = 'product_list'
    template_name = 'product_list.html'

    def get_queryset(self):
        queryset = super(ProductList, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        # context['extra_url_param'] = urlencode({'show': self.show, 'my': self.my, 'state': self.state})
        return context


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        # context["form"] = ProductForm(instance=self.object)
        # context['extra_url_param'] = urlencode({'show': self.show, 'my': self.my, 'state': self.state})
        return context


class ProductCreate(CreateView):
    model = POrder
    form_class = ProductForm
    template_name = 'product-form.html'
    success_url = reverse_lazy('product_list')
    # permission_required = 'task.add_task'

    def form_valid(self, form):
        return super(ProductCreate, self).form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product-form.html'
    # permission_required = 'task.change_task'

    def get_success_url(self):
        return self.object.get_absolute_url()

    # def get_form(self, form_class=None):
    #     form = super(ProductUpdate, self).get_form(form_class=form_class)
    #     ice_apps = form.fields['ice_app']
    #     form.fields['ice_app'].queryset = ice_apps.queryset.filter(users=self.request.user).all()
    #     return form


class OrderList(ListView):
    model = POrder
    paginate_by = 12
    context_object_name = 'order_list'
    template_name = 'order_list.html'

    def get_queryset(self):
        queryset = super(OrderList, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        # context['extra_url_param'] = urlencode({'show': self.show, 'my': self.my, 'state': self.state})
        return context


class OrderDetail(DetailView):
    model = POrder
    context_object_name = 'order'
    template_name = 'order-detail.html'

    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        # context["form"] = OrderForm(instance=self.object)
        # context['extra_url_param'] = urlencode({'show': self.show, 'my': self.my, 'state': self.state})
        return context


class OrderCreate(CreateView):
    model = POrder
    form_class = OrderForm
    template_name = 'order-form.html'
    success_url = reverse_lazy('order_list')
    # permission_required = 'task.add_task'

    def form_valid(self, form):
        return super(OrderCreate, self).form_valid(form)


class OrderUpdate(UpdateView):
    model = POrder
    form_class = OrderForm
    template_name = 'order-form.html'
    # permission_required = 'task.change_task'

    def get_success_url(self):
        return self.object.get_absolute_url()
