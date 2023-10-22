import json

from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open("catalog_data.json", 'r', encoding='utf-8') as f:
            items = json.load(f)

        categories_for_create = []
        products_for_create = []
        for item in items:
            if item['model'] == 'catalog.category':
                categories_for_create.append(Category(pk=item['pk'], **item['fields']))

        for item in items:
            if item['model'] == 'catalog.category':
                continue
            for category in categories_for_create:
                if category.pk == item['fields']['category']:
                    item['fields']['category'] = category
            products_for_create.append(Product(pk=item['pk'], **item['fields']))

        Category.objects.bulk_create(categories_for_create)
        Product.objects.bulk_create(products_for_create)
