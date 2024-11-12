from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from orders.admin import OrderTabulareAdmin
from carts.admin import CartTabAdmin
# Register your models here.
from .forms import UserLoginForm, UserRegisterForm
from users.models import CustomUser
# Register your models here.

User= get_user_model()

#admin.site.register(CustomUser,UserAdmin)



#admin.site.register(Products)

@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display =['username', 'first_name', 'email',]
    search_fields=['username', 'email']
    # Связь с моделью Cart через inline
    inlines = [CartTabAdmin,OrderTabulareAdmin]  # Inline для отображения корзины
    
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2'),
    }),
)
    add_form=UserRegisterForm