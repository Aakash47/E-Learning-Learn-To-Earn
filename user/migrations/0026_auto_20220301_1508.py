# Generated by Django 3.1.4 on 2022-03-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20220301_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]