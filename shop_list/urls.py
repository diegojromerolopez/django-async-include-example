from django.urls import path

from shop_list import views

app_name = 'shop_list'
urlpatterns = [
    # /shop_lists/
    path('', views.index, name='index'),
    # /shop_list/5/
    path('<int:shop_list_id>/', views.shop_list, name='shop_list'),
]
