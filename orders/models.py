# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class POrder(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    order_limit = models.IntegerField(blank=True, null=True)
    order_term = models.IntegerField(blank=True, null=True)
    order_interest = models.FloatField(blank=True, null=True)
    order_fee_sum = models.IntegerField(blank=True, null=True)
    order_actual_money = models.IntegerField(blank=True, null=True)
    order_repay_money = models.IntegerField(blank=True, null=True)
    order_apply_time = models.IntegerField(blank=True, null=True)
    order_approval_time = models.IntegerField(blank=True, null=True)
    order_lend_time = models.IntegerField(blank=True, null=True)
    order_appointment_repay_time = models.IntegerField(blank=True, null=True)
    order_actual_repay_time = models.IntegerField(blank=True, null=True)
    order_status = models.IntegerField(blank=True, null=True)
    bind_card_status = models.IntegerField(blank=True, null=True)
    create_time = models.BigIntegerField()
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_order'

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('order_update', kwargs={'pk': self.pk})


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=64)
    product_logo = models.CharField(max_length=1024)
    product_limit_desc = models.CharField(max_length=512)
    product_min_limit = models.IntegerField()
    product_max_limit = models.IntegerField()
    product_limit_unit = models.CharField(max_length=64)
    product_limit_size = models.IntegerField()
    product_speed_desc = models.CharField(max_length=512)
    product_term_desc = models.CharField(max_length=512)
    product_min_term = models.IntegerField()
    product_max_term = models.IntegerField(blank=True, null=True)
    product_term_unit = models.CharField(max_length=64)
    product_term_size = models.IntegerField()
    product_interest_desc = models.CharField(max_length=512)
    product_ads_desc = models.CharField(max_length=512)
    product_activity_desc = models.CharField(max_length=512)
    repay_url = models.CharField(max_length=512, blank=True, null=True)
    bind_card_url = models.CharField(max_length=512, blank=True, null=True)
    status = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)
    create_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'product'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('product_update', kwargs={'pk': self.pk})