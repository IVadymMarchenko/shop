from django.contrib import admin

# Register your models here.
from .models import Cart

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User= get_user_model()


class CartTabAdmin(admin.TabularInline):
    # Указываем модель, с которой работает данный класс.
    model = Cart
    
    # Это позволит показывать столбцы для продукта, количества и времени создания.
    fields = ['product', 'quantity', 'created_timestamp']
    
    # Определяем поля, по которым можно будет искать в админке.
    search_fields = ['product__name', 'quantity', 'created_timestamp']

    # Указываем поля которые будут доступны только для просмотра и не подлежат редактированию.
    readonly_fields = ['created_timestamp']

    # Указываем, сколько пустых форм для добавления новых объектов Cart будет отображаться.
    extra = 1
    
    def product_display(self,obj):
        return str(obj.product.name)



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product__name','quantity','created_timestamp']
    list_filter= ['product__name','quantity','created_timestamp']
    
    
    def user_display(self,obj):
        if obj.user:
            return str(obj.user)
        return 'Анонімний користувач'
    
 
        





