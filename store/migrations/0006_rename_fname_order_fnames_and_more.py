# Generated by Django 4.0.6 on 2022-10-15 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='fname',
            new_name='fnames',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='products',
        ),
    ]
