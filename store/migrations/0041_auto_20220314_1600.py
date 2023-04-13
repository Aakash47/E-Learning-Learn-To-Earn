# Generated by Django 3.1.4 on 2022-03-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_order_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='seller',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('merch', 'Merch'), ('book', 'Book')], default='book', max_length=10),
        ),
    ]