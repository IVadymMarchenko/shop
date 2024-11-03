from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse
from .models import Products,Categories
from django.core.paginator import Paginator
from django.db.models import Q
from .dbfilters import GetProduct,FilterProduct,q_search_products  

# Create your views here.

def catalog(request,category_slug=None):
    
    page=request.GET.get('page','1')
    query=request.GET.get('q',None)
    
    if category_slug == 'All':
        goods = Products.objects.all()
    elif query:
        goods = q_search_products(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)
     
    filters = Q()
    fields_for_filter = ['producer', 'processor_model', 'videocard_model', 'ram', 'storage_type']
      
    for field in fields_for_filter:
        values = request.GET.getlist(field)
        if values:
            filters &= Q(**{f'{field}__in': values})
            
    #if category_slug == 'All':
        #goods = Products.objects.all()
    #else:
        #goods = Products.objects.filter(Q(category__slug=category_slug) | filters)
            
    goods = goods.filter(filters) if filters else goods
    
    paginator=Paginator(goods,3)
    curent_page = paginator.page(int(page))
    
    context = {
        'items': curent_page,
        'slug_url': category_slug,      
    }
    return render(request, 'goods/catalog.html', context=context)





def product(request,product_slug):
    
    product = Products.objects.get(slug=product_slug)
    
    context= { 
              'product': product
              }
    
    return render(request, 'goods/product.html',context=context)
