from django.shortcuts import render, get_object_or_404

from shop_list.models import ShopList

DEFAULT_SHOP_LIST_SIZE = 100
SHOP_LIST_SIZES = [20, 50, 100]


def index(request):
    shop_list_size = int(request.GET.get('size', DEFAULT_SHOP_LIST_SIZE))
    shop_lists = ShopList.objects.all().order_by('-created_at')[:shop_list_size]
    replacements = {'shop_lists': shop_lists, 'sizes': SHOP_LIST_SIZES}
    return render(request, 'shop_list/index.html', replacements)


def shop_list(request, shop_list_id):
    shop_list = get_object_or_404(ShopList, id=shop_list_id)
    replacements = {'shop_list': shop_list, 'items': shop_list.item_set.all}
    return render(request, 'shop_list/shop_list.html', replacements)
