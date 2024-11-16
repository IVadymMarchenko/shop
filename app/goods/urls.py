from django.urls import path

from . import views



app_name = 'goods'


urlpatterns = [
     path("seach/", views.CatalogView.as_view(), name="seach"),
     path("<slug:category_slug>/", views.CatalogView.as_view(), name="goods"),
     path("product/<slug:product_slug>/", views.ProductView.as_view(), name="product"),
     
     ]