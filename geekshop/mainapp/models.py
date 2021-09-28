from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=64, unique=True)
    en_name = models.SlugField(verbose_name='имя категории на английском', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class ProductBootstrapMixin:
    @staticmethod
    def _get_image(img_url, file_name):
        from django.conf import settings
        import requests

        path_for_save = f'{settings.MEDIA_ROOT}/products_images/'
        f = open(f'{path_for_save}{file_name}.jpg', 'wb')
        f.write(requests.get(img_url).content)
        f.close()
        path_for_get = f'products_images/{file_name}.jpg'
        return path_for_get

    @staticmethod
    def _bootstrap(count=5, locale='ru'):
        from mimesis import Internet
        from random import randint
        from mimesis import Text
        from mimesis.random import get_random_item

        categories = ProductCategory.objects.all()
        img_url = Internet().stock_image(width=300, height=400)

        for _ in range(count):
            image_name = Text('en').word()

            product = Product(
                category=get_random_item(categories),
                name=Text('ru').word(),
                image=Product._get_image(img_url, image_name),
                short_desc=' '.join(Text('ru').words(7)),
                description=' '.join(Text('ru').words(17)),
                price=randint(100, 10000),
                quantity=randint(1, 100)
            )
            product.save()


class Product(ProductBootstrapMixin, models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
