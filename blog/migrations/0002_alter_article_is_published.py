# Generated by Django 4.2.6 on 2023-10-31 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='флаг публикации'),
        ),
    ]
