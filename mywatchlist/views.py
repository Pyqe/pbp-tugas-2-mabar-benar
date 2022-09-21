from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchList

def show_html(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'list_watchlist': data_watchlist,
        'nama': 'Pikatan Arya Bramajati',
        'npm': '2106630031'
    }
    return render(request, "mywatchlist.html", context)


def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")