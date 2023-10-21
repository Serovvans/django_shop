from django.db import models

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

    def __str__(self):
        return f"{self.name} - {self.category} - {self.price}"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
