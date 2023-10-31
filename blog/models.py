from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='заголовок')
    slug = models.CharField(**NULLABLE, max_length=500, verbose_name='слаг')
    text = models.TextField(verbose_name='текст')
    preview = models.ImageField(**NULLABLE, verbose_name='превью')
    create_date = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='флаг публикации')
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}\n{self.text}"

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
