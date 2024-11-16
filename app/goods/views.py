from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse
from .models import Products,Categories
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .dbfilters import GetProduct,FilterProduct,q_search_products  

# Create your views here.


class CatalogView(ListView):
    model = Products
    #queryset=Products.objects.all().order_by('id') дополнительние фильтры
    template_name = 'goods/catalog.html'
    context_object_name = 'items'
    paginate_by = 3

    def get_queryset(self):
        # Получаем slug категории
        category_slug = self.kwargs.get('category_slug')
        # Получаем поисковый запрос, если он есть
        query = self.request.GET.get('q', None)
        # Базовый набор товаров
        if category_slug == 'All':
            goods = super().get_queryset()
        elif query:
            goods = q_search_products(query)  #  функц возвращ QuerySet
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)

        # Фильтры
        filters = Q()
        fields_for_filter = ['producer', 'processor_model', 'videocard_model', 'ram', 'storage_type']
        for field in fields_for_filter:
            values = self.request.GET.getlist(field)
            if values:
                filters &= Q(**{f'{field}__in': values})
        
        # Применение фильтров
        goods = goods.filter(filters) if filters else goods
        return goods

    def get_context_data(self, **kwargs):
        # Получение базового контекста
        context = super().get_context_data(**kwargs)
        # Добавление slug категории
        context['category_slug'] = self.kwargs.get('category_slug')  # Исправлено
        #context['categories']=Categories.objects.all() # просто пердаем в контекст допол данные
        return context



class ProductView(DetailView):
    #model = Products
    template_name = 'goods/product.html'
    slug_url_kwarg='product_slug' # slug_url_kwarg спец поле для получения slug
    context_object_name = 'product'
     
    def get_object(self, queryset = None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    
    def get_context_data(self, **kwargs):
        contex=super().get_context_data(**kwargs)
        contex['title'] = self.object.name
        return super().get_context_data(**kwargs)



#def catalog(request,category_slug=None):
    
    #page=request.GET.get('page','1')
    #query=request.GET.get('q',None)
    
    #if category_slug == 'All':
        #goods = Products.objects.all()
    #elif query:
        #goods = q_search_products(query)
    #else:
        #goods = Products.objects.filter(category__slug=category_slug)
     
    #filters = Q()
    #fields_for_filter = ['producer', 'processor_model', 'videocard_model', 'ram', 'storage_type']
      
    #for field in fields_for_filter:
        #values = request.GET.getlist(field)
        #if values:
            #filters &= Q(**{f'{field}__in': values})
            
    ##if category_slug == 'All':
        #goods = Products.objects.all()
    ##else:
        ##goods = Products.objects.filter(Q(category__slug=category_slug) | filters)
            
    #goods = goods.filter(filters) if filters else goods
    
    #paginator=Paginator(goods,3)
    #curent_page = paginator.page(int(page))
    
    #context = {
        #'items': curent_page,
        #'slug_url': category_slug,      
    #}
    #return render(request, 'goods/catalog.html', context=context)





#def product(request,product_slug):
    #product = Products.objects.get(slug=product_slug) 
    #context= { 
              #'product': product
              #}
    #return render(request, 'goods/product.html',context=context)
