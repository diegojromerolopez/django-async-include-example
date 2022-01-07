from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models.query import QuerySet
from shop_list.models import ShopList

DEFAULT_SHOP_LIST_SIZE = 100
SHOP_LIST_SIZES = [20, 50, 100]


def index(request: HttpRequest) -> HttpResponse:
    shop_list_size = int(request.GET.get('size', DEFAULT_SHOP_LIST_SIZE))
    shop_lists: QuerySet[ShopList] = ShopList.objects.all().order_by('-created_at')[:shop_list_size]
    replacements = {'shop_lists': shop_lists, 'sizes': SHOP_LIST_SIZES}
    template_path = 'shop_list/index.html'
    return render(request, template_path, replacements)


def view_shop_list(request: HttpRequest, shop_list_id: int) -> HttpResponse:
    shop_list = get_object_or_404(ShopList, id=shop_list_id)
    replacements = {'shop_list': shop_list, 'items': shop_list.item_set.all}
    return render(request, 'shop_list/view_shop_list.html', replacements)
