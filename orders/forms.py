# -*- coding: utf-8 -*-
from django.forms import ModelForm

from models import POrder, Product


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    #     exclude = ['user', 'vercode', 'superior', 'permission', 'add_role_perm', 'vacation_manager', 'dinner_manager', 'user_manger', 'apply_subject_perm']
    # superior = forms.CharField(widget=forms.TextInput, label='上级邮箱')
    # status = forms.BooleanField(widget=forms.CheckboxInput, label='在职状态', required=False)


class OrderForm(ModelForm):

    class Meta:
        model = POrder
        fields = '__all__'
