from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    preview = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='превью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за покупку')
    create_data = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    update_data = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='дата последнего изменения')

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return f"{self.name} - {self.category} - {self.price}"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        permissions = [
            (
                'set_is_published',
                'Can publish post'
            ),
            (
                'set_description',
                'Can change description'
            ),
            (
                'set_category',
                'Can change category'
            )
        ]


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    phone = models.CharField(max_length=12, verbose_name='телефон')
    message = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return f"{self.message}"

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    num_version = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(**NULLABLE, max_length=150, verbose_name='название')
    is_current = models.BooleanField(verbose_name='текущая версия')

    def __str__(self):
        return f"{self.num_version} -> {self.name}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
