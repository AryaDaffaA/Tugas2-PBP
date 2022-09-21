from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def watchlist(request):
    data_watchlist = MyWatchList.objects.all()
    subject = {
        'myWatchList': data_watchlist,
        'nama': 'Arya Daffa',
        'NPM': '2106650853',
    }  
    return render(request, "watchlist.html", subject)

def xml_funct(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def json_funct(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def id_funct_xml(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def id_funct_json(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")