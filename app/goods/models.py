from django.db import models
from django.urls import reverse

# Create your models here.
#venv\Scripts\activate
#python manage.py dumpdata goods.Categoryies > fixtures/goods/base.json     --для сохран базы в json




class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="назва")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорію' # для отображения названия табл в адм панеле
        verbose_name_plural = 'Категорія' # для отображения названия табл в адм панеле
        
    def __str__(self):
        return self.name  # для отображения названия в адм панеле
        
        

class Products(models.Model):
    producer = models.CharField(max_length=255, default='не відомий виробник',blank=True, null=True, verbose_name='Виробник',)
    name = models.CharField(max_length=150, unique=True, verbose_name="назва")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True,verbose_name='Опис')
    image=models.ImageField(upload_to='goods_images',blank=True, null=True, verbose_name='фото',)
    price=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='ціна')
    discout=models.DecimalField(default=0.00,max_digits=7,decimal_places=2,verbose_name='знижка')
    category= models.ForeignKey(to=Categories, on_delete=models.CASCADE,verbose_name='категорія') #models.PROTECT models.SET_DEFAULT
    sales_count = models.PositiveIntegerField(default=0, verbose_name='Кількість продажів')
    count = models.PositiveIntegerField(default=0, verbose_name='Залишок на складі') 
    
    # Характеристики экрана
    screen_size = models.CharField(max_length=50, blank=True, null=True, verbose_name='Діагональ екрану')
    screen_refresh_rate = models.CharField(max_length=50, blank=True, null=True, verbose_name='Частота оновлення екрану')
    screen_type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип екрану')
    screen_resolution = models.CharField(max_length=50, blank=True, null=True, verbose_name='Роздільна здатність')
    screen_coverage = models.CharField(max_length=50, blank=True, null=True, verbose_name='Покриття екрану')

    # Характеристики процессора
    processor_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Модель процесора')
    processor_frequency = models.CharField(max_length=50, blank=True, null=True, verbose_name='Частота процесора')
    processor_generation = models.CharField(max_length=50, blank=True, null=True, verbose_name='Покоління процесора')

    # Характеристики оперативной памяти
    ram = models.CharField(max_length=50, blank=True, null=True, verbose_name="Об'єм оперативної пам'яті")

    # Характеристики видеокарты
    videocard_model = models.CharField(max_length=150, blank=True, null=True, verbose_name='Модель відеокарти')
    videocard_memory = models.CharField(max_length=50, blank=True, null=True, verbose_name="Об'єм пам'яті відеокарти")

    # Характеристики накопителя
    storage_type = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип накопичувача')
    storage_capacity = models.CharField(max_length=50, blank=True, null=True, verbose_name="Об'єм накопичувача")

    # характеристики батареи и камеры
    battery = models.CharField(max_length=100, blank=True, null=True, verbose_name='Батарея')
    camera = models.CharField(max_length=100, blank=True, null=True, verbose_name='Камера')

    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категорія') 
    
    
    class Meta:
        db_table = 'product'
        verbose_name = 'продукт' # для отображения названия табл в адм панеле
        verbose_name_plural = 'продукт' # для отображения названия табл в адм панеле
        ordering =('id',) # сортировка товаров по id
    
    def __str__(self):
        return f'{self.name} Кількість - {self.count}'  # для отображения названия в адм панеле
    
    def get_absolute_url(self):# метод для админки кнопка перехода для просмотра товара
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    
    
    def display_id(self):
        return f'{self.id:05}' #self.id:05 добавим нули к айди чтобы сумарное значение было 5 символов
    
    
    def sell_price(self):
        if self.discout:
            return round(self.price - self.price*self.discout/100,2)
        return self.price
        
    
