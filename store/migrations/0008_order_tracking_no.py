# Generated by Django 4.0.6 on 2022-10-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_fnames_order_fname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tracking_no',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
