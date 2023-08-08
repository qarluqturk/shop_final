# Generated by Django 4.2.1 on 2023-08-01 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_product_image3_remove_product_image4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='post', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='product', to=settings.AUTH_USER_MODEL),
        ),
    ]
