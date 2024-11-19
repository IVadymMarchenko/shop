from django.urls import path

from . import views



app_name = 'orders'


urlpatterns = [
     path("get-departments/", views.GetDepartmentsView.as_view(), name="get_departments"),
     path("create_order/", views.CreateOrderView.as_view(), name="create_order"), 
     path('get-cities/', views.GetCitiesView.as_view(), name='get-cities'),  
]