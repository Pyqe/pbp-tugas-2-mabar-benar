from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        "catalog_item_list": data_catalog_item,
        "name": "Pikatan Arya Bramajati",
        "npm": "2106630031"
    }
    return render(request, "katalog.html", context)