# Generated by Django 5.1.2 on 2024-11-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
            options={
                'verbose_name': 'Проданний товар',
                'verbose_name_plural': 'Продані товари',
                'db_table': 'order_item',
            },
        ),
    ]
