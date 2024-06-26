# Generated by Django 5.0.4 on 2024-04-18 09:40

import enumchoicefield.fields
import motel.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motel', '0009_motel_furniture_alter_motel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='label',
            field=enumchoicefield.fields.EnumChoiceField(enum_class=motel.models.PriceEnum, max_length=11),
        ),
    ]
