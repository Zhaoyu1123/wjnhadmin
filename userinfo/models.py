# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    phone = models.CharField(unique=True, max_length=64)
    create_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class UserCallRecords(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    phone = models.CharField(max_length=64)
    trade_type = models.IntegerField()
    trade_time = models.CharField(max_length=20, blank=True, null=True)
    call_time = models.CharField(max_length=20, blank=True, null=True)
    receive_phone = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_call_records'


class UserCheckIdcardInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=64)
    idcard = models.CharField(max_length=64)
    address = models.CharField(max_length=255, blank=True, null=True)
    issuing = models.CharField(max_length=128, blank=True, null=True)
    idcard_passed_time = models.BigIntegerField(blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_check_idcard_info'


class UserContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    contact_phone = models.CharField(max_length=64)
    contact_name = models.CharField(max_length=64)
    relation = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_contact'


class UserContactsPhone(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    contact_phone = models.CharField(max_length=64)
    contact_name = models.CharField(max_length=64)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_contacts_phone'


class UserFaceInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    face_type = models.IntegerField()
    face_url = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_face_info'


class UserFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    content = models.TextField(blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_feedback'


class UserIdcardInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=64)
    idcard = models.CharField(max_length=64)
    race = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    idcard_url_positive = models.CharField(max_length=128, blank=True, null=True)
    issuing = models.CharField(max_length=128, blank=True, null=True)
    idcard_passed_time = models.BigIntegerField(blank=True, null=True)
    idcard_url_negative = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_idcard_info'


class UserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    social_identity = models.IntegerField(blank=True, null=True)
    expected_amount = models.CharField(max_length=50, blank=True, null=True)
    current_live_address = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.IntegerField()
    education_level = models.IntegerField()
    company_name = models.CharField(max_length=128, blank=True, null=True)
    salary = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class UserSms(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    phone = models.CharField(max_length=64)
    sms_type = models.IntegerField()
    sms_date = models.CharField(max_length=20, blank=True, null=True)
    send_centent = models.CharField(max_length=2048, blank=True, null=True)
    sms_phone = models.CharField(max_length=64)
    sms_name = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_sms'


class IspPhoneBill(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    phone = models.CharField(max_length=64)
    month = models.CharField(max_length=20, blank=True, null=True)
    call_pay = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isp_phone_bill'


class IspPhoneCall(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    phone = models.CharField(max_length=64)
    trade_type = models.IntegerField()
    trade_time = models.CharField(max_length=20, blank=True, null=True)
    call_time = models.CharField(max_length=20, blank=True, null=True)
    receive_phone = models.CharField(max_length=64)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isp_phone_call'


class IspPhoneSms(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    phone = models.CharField(max_length=64)
    sms_type = models.IntegerField()
    sms_date = models.CharField(max_length=20, blank=True, null=True)
    sms_phone = models.CharField(max_length=64)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isp_phone_sms'


class IspUserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    phone = models.CharField(max_length=64)
    phone_service_password = models.CharField(max_length=16, blank=True, null=True)
    user_source = models.CharField(max_length=30, blank=True, null=True)
    real_name = models.CharField(max_length=64)
    idcard = models.CharField(max_length=64)
    phone_remain = models.CharField(max_length=255, blank=True, null=True)
    reg_time = models.CharField(max_length=64, blank=True, null=True)
    isp = models.CharField(max_length=4, blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isp_user_info'
