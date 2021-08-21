from django.contrib import admin
from django.urls import path, include

from shop_list import views as shop_list_views

urlpatterns = [
    path('', shop_list_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('shop_list/', include('shop_list.urls')),
    path(r'async_include/', include('async_include.urls', namespace="async_include")),
]
