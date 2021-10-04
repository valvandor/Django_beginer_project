import json
import os

from authapp.models import ShopUser
from django.core.management.base import BaseCommand

from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # categories = load_from_json('categories')
        # ProductCategory.objects.all().delete()
        # for category in categories:
        #     new_category = ProductCategory(**category)
        #     new_category.save()

        Product._bootstrap()

        # Удаляем пользователя, если он существует
        ShopUser.objects.filter(username="valvandor", is_superuser=True).delete()
        # Создаем суперпользователя при помощи менеджера модели
        ShopUser.objects.create_superuser(username='valvandor', password='geekbrains', date_birthday='1994-02-23')
