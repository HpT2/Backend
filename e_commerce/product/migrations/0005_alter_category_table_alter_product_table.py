# Generated by Django 4.0.8 on 2022-12-02 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_delete_image_alter_category_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='[product].[category]',
        ),
        migrations.AlterModelTable(
            name='product',
            table='[product].[product]',
        ),
    ]
