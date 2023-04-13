# Generated by Django 3.1.4 on 2022-02-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20220224_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='resource',
            field=models.FileField(upload_to='static/resources'),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(upload_to='static/thumbnail'),
        ),
    ]