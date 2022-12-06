# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Product(models.Model):
    product_id = models.IntegerField(db_column='Product_ID',primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_name', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    product_desc = models.CharField(db_column='Product_desc', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    category_id = models.IntegerField(db_column='Category_ID', blank=True, null=True)  # Field name made lowercase.
    admin_id = models.CharField(db_column='Admin_ID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    product_img = models.ImageField(db_column='Product_IMG', blank=True, upload_to='static/img/product')

    def __int__(self,img,name,price):
        self.price=price
        self.product_name=name
        self.product_img=img

    class Meta:
        managed = False
        db_table = '[product].[product]'


class Category(models.Model):
    category_id = models.IntegerField(db_column='Category_ID',primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='Category_name', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    category_img = models.BinaryField(db_column='Category_img', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[product].[category]'
