from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from goods.models import Categories,Products
# Create your views here.



class TopSalesView(TemplateView):
  template_name = 'main/index.html'
  
  def get_context_data(self, **kwargs):
        # Получаем базовый контекст от родительского класса
        context = super().get_context_data(**kwargs)
        
        # Добавляем список товаров, отсортированных по количеству продаж
        context['items'] = Products.objects.order_by('-sales_count')[:10]
        
        # Возвращаем контекст для использования в шаблоне
        return context
  






#def top_sales(request):
  
  #top_sales= Products.objects.order_by('-sales_count')[:10]
    
  #context = {
        #'items': top_sales
    #}
  #return render(request, 'main/index.html', context=context)