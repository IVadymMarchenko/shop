from .models import Products
from django.views.generic.list import ListView
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    SearchHeadline,
)


class GetProduct(ListView):
    """для вивод всех продуктов"""

    def get_producer(self):
        return Products.objects.values_list("producer", flat=True).distinct()


class FilterProduct(GetProduct, ListView):

    def get_queryset(self):
        queryset = Products.objects.filter(
            producer__in=self.request.GET.getlist("producer")
        )
        return queryset


def q_search_products(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )  # поиск от джанго (окончательн) (filter(rank__gt=0)если проц совпадениея больше 0)
    
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel="<span style='background-color:yellow;'>",
            stop_sel='</span>',
        )
    )  # для выдел текста(поиска) на страниц
    result = result.annotate(
        headline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        )
    )  # для выдел текста(поиска) на страниц
    return result

    # return Products.objects.annotate(search=SearchVector("name", "description")).filter(search=query)  # поиск от джанго (прод)
    # return Products.objects.filter(name__search=query) # поиск от джанго (обчн)

    # keywords = [word for word in query.split() if len(word)>2]
    # filters = Q()
    # for token in keywords:
    # filters |= Q(description__icontains=token)
    # filters |= Q(name__icontains=token)
    # return Products.objects.filter(filters)
