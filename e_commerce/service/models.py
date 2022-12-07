# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    customer_id = models.CharField(db_column='Customer_ID',primary_key=True, max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    middle_name = models.CharField(db_column='Middle_name', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    birthdate = models.DateField(db_column='Birthdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[service].[customer]'


class Feedback(models.Model):
    customer_id = models.CharField(db_column='Customer_ID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    product_id = models.IntegerField(db_column='Product_ID',primary_key = True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    star = models.IntegerField(db_column='Star')  # Field name made lowercase.
    datepost = models.DateField(db_column='Datepost')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[service].[feedback]'


class Cart(models.Model):
    cart_id = models.IntegerField(db_column='Cart_ID',primary_key = True)  # Field name made lowercase.
    total_price = models.FloatField(db_column='Total_price')  # Field name made lowercase.
    customer_id = models.CharField(db_column='Customer_ID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[service].[cart]'


class Contain(models.Model):
    product_id = models.IntegerField(db_column='Product_ID',primary_key = True)  # Field name made lowercase.
    cart_id = models.IntegerField(db_column='Cart_ID')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[service].[contain]'


class Orders(models.Model):
    order_id = models.CharField(db_column='Order_ID',primary_key = True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    order_date = models.DateField(db_column='Order_date')  # Field name made lowercase.
    discount = models.FloatField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    total_price = models.FloatField(db_column='Total_price')  # Field name made lowercase.
    delivery = models.BooleanField(db_column='Delivery', blank=True, null=True)  # Field name made lowercase.
    cart_id = models.IntegerField(db_column='Cart_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[service].[orders]'
