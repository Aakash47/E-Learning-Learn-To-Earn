# Generated by Django 3.1.4 on 2022-02-15 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20220215_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]