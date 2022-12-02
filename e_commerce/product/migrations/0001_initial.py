# Generated by Django 4.0.8 on 2022-11-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField(db_column='Category_ID')),
                ('category_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Category_name', max_length=10)),
                ('category_img', models.BinaryField(blank=True, db_column='Category_img', max_length='max', null=True)),
            ],
            options={
                'db_table': '[product].[category]',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(db_column='Product_ID')),
                ('product_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Product_name', max_length=10)),
                ('product_desc', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Product_desc', max_length=30, null=True)),
                ('price', models.FloatField(db_column='Price')),
                ('product_img', models.BinaryField(blank=True, db_column='Product_img', max_length='max', null=True)),
                ('amount', models.IntegerField(blank=True, db_column='Amount', null=True)),
                ('category_id', models.IntegerField(blank=True, db_column='Category_ID', null=True)),
                ('admin_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Admin_ID', max_length=5)),
            ],
            options={
                'db_table': '[product].[product]',
                'managed': False,
            },
        ),
    ]
