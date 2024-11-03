from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories,Products
# Create your views here.



def top_sales(request):
  
  top_sales= Products.objects.order_by('-sales_count')[:10]
    
  context = {
        'items': top_sales
    }
  return render(request, 'main/index.html', context=context)

