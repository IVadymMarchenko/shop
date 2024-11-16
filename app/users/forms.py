from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password']  

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise ValidationError("Invalid email or password.")
        return cleaned_data


        
class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model=CustomUser
        fields=['username', 'email', 'password1', 'password2']
    
    username=forms.CharField()
    email=forms.CharField()
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    













    
# class UserLoginForm(forms.Form):
#     email = forms.EmailField(label="Email", max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput, label="Password")
#     user = None  # Хранение аутентифицированного пользователя

#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)
#         super().__init__(*args, **kwargs)

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email')
#         password = cleaned_data.get('password')

#         if email and password:
#             user = authenticate(self.request, email=email, password=password)
#             if user is None:
#                 raise ValidationError("Invalid email or password.")
#             if not user.is_active:
#                 raise ValidationError("This account is inactive.")
#             self.user = user  # Сохраняем пользователя
#         return cleaned_data

#     def get_user(self):
#         return self.user  # Возвращаем аутентифицированного пользователя это заработало! Но не высвечиваеться сообщение это  messages.success(request, f'{email}, login is successful')