# Generated by Django 5.1.2 on 2024-11-10 21:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення замовлення')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Телефон')),
                ('requires_delivery', models.BooleanField(default=False, verbose_name='Потрібна доставка')),
                ('delivery_address', models.TextField(max_length=255, verbose_name='Адреса доставки')),
                ('payment', models.BooleanField(default=False, verbose_name='Оплата при отриманні')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплаченно')),
                ('status', models.CharField(default='в обробці', max_length=50, verbose_name='Статус замовлення')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Ціна')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кількість')),
                ('created_timesramp', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажу')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Замовлення')),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Проданний товар',
                'verbose_name_plural': 'Продані товари',
                'db_table': 'order_item',
            },
        ),
    ]
