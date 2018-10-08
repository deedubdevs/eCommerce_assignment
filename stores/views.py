from django.shortcuts import render
from .models import StoreItems


def browse(request, store_id):
    store_items = StoreItems.objects.filter(store_id=store_id)
    context = {"store_items": store_items}
    return render(request, "stores/browse.html", context)
