# Generated by Django 2.2 on 2020-04-20 01:58

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='receta',
            field=jsonfield.fields.JSONField(max_length=200),
        ),
    ]
