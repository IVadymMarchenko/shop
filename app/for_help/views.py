from django.shortcuts import redirect, render
from .models import ForHelp
from .forms import HelpForm
from django.contrib import messages
# Create your views here.


def for_help(request):
    form = HelpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Сохраняем данные в БД
            form.save()
            # Сообщение об успешной отправке
            messages.success(request, "Ми зв'яжемося з вами найближчим часом")
            # Перенаправление на главную страницу
            return redirect('main:main')
        else:
            # Если форма не валидна, ошибки автоматически передаются в шаблон
            return render(request, 'main/for_help_window.html', {'form': form})

    # Если GET-запрос
    return render(request, 'main/for_help_window.html', {'form': form})
    