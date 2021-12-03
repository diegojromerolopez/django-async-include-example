from django.shortcuts import render, get_object_or_404

from shop_list.models import ShopList


def index(request):
    shop_lists = ShopList.objects.all().order_by('-created_at')[:50]
    return render(request, 'shop_list/index.html', {'shop_lists': shop_lists})


def shop_list(request, shop_list_id):
    shop_list = get_object_or_404(ShopList, id=shop_list_id)
    replacements = {'shop_list': shop_list, 'items': shop_list.item_set.all}
    return render(request, 'shop_list/shop_list.html', replacements)
