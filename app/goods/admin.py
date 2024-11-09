from django.contrib import admin

# Register your models here.
from goods.models import Categories,Products
# Register your models here.


#admin.site.register(Categories)
#admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # поля которые запол автоматич
    list_display =['name',]
    
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display=['name','count','price','discout',] # отображен полей в админке
    list_editable=['price','discout',] # поля которые можно редактир в админке
    search_fields=['name','description'] # поля поиска в админке
    list_filter = ['discout','count','category']  # поля фильтрац в админке
    fields = ['name','category','slug','description','image',('price','discout'),'count']