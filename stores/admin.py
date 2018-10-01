from django.contrib import admin
from .models import Item, Store, StoreItems

admin.site.register(Item)
admin.site.register(Store)
admin.site.register(StoreItems)
