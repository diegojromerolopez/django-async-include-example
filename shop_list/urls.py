from django.urls import path

from shop_list import views

app_name = 'shop_list'
urlpatterns = [
    # /shop_lists/
    path('', views.index, name='index'),
    # /shop_list/5/
    path('<int:shop_list_id>/', views.view_shop_list, name='view_shop_list'),
]
