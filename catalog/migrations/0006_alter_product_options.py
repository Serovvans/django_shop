# Generated by Django 4.2.6 on 2023-11-26 14:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0005_product_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "permissions": [
                    ("set_is_published", "Can publish post"),
                    ("set_description", "Can change description"),
                    ("set_category", "Can change category"),
                ],
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
            },
        ),
    ]
