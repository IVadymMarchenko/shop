from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
from .forms import UserLoginForm, UserRegisterForm
from users.models import CustomUser
# Register your models here.

User= get_user_model()

#admin.site.register(CustomUser,UserAdmin)



#admin.site.register(Products)

@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2'),
    }),
)
    add_form=UserRegisterForm