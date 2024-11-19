from django.contrib import admin

from .models import ForHelp

# Register your models here.





@admin.register(ForHelp)
class ProductsAdmin(admin.ModelAdmin):
    list_display=['id','name','phone',] # отображен полей в админке
    list_editable=['name','phone',] # поля которые можно редактир в админке
    search_fields=['name','phone'] # поля поиска в админке
    list_filter = ['created_timestamp']  # поля фильтрац в админке
  