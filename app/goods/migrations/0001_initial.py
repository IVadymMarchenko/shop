# Generated by Django 5.1.2 on 2024-11-17 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорію',
                'verbose_name_plural': 'Категорія',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer', models.CharField(blank=True, default='не відомий виробник', max_length=255, null=True, verbose_name='Виробник')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='фото')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='ціна')),
                ('discout', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='знижка')),
                ('sales_count', models.PositiveIntegerField(default=0, verbose_name='Кількість продажів')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Залишок на складі')),
                ('screen_size', models.CharField(blank=True, max_length=50, null=True, verbose_name='Діагональ екрану')),
                ('screen_refresh_rate', models.CharField(blank=True, max_length=50, null=True, verbose_name='Частота оновлення екрану')),
                ('screen_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип екрану')),
                ('screen_resolution', models.CharField(blank=True, max_length=50, null=True, verbose_name='Роздільна здатність')),
                ('screen_coverage', models.CharField(blank=True, max_length=50, null=True, verbose_name='Покриття екрану')),
                ('processor_model', models.CharField(blank=True, max_length=100, null=True, verbose_name='Модель процесора')),
                ('processor_frequency', models.CharField(blank=True, max_length=50, null=True, verbose_name='Частота процесора')),
                ('processor_generation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Покоління процесора')),
                ('ram', models.CharField(blank=True, max_length=50, null=True, verbose_name="Об'єм оперативної пам'яті")),
                ('videocard_model', models.CharField(blank=True, max_length=150, null=True, verbose_name='Модель відеокарти')),
                ('videocard_memory', models.CharField(blank=True, max_length=50, null=True, verbose_name="Об'єм пам'яті відеокарти")),
                ('storage_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип накопичувача')),
                ('storage_capacity', models.CharField(blank=True, max_length=50, null=True, verbose_name="Об'єм накопичувача")),
                ('battery', models.CharField(blank=True, max_length=100, null=True, verbose_name='Батарея')),
                ('camera', models.CharField(blank=True, max_length=100, null=True, verbose_name='Камера')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукт',
                'db_table': 'product',
                'ordering': ('id',),
            },
        ),
    ]
