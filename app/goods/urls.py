from django.urls import path

from . import views



app_name = 'goods'


urlpatterns = [
     path("seach/", views.catalog, name="seach"),
     path("<slug:category_slug>/", views.catalog, name="goods"),
     path("product/<slug:product_slug>/", views.product, name="product"),
     
     ]