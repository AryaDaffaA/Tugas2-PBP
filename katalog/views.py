from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def show_catalog(request):
    data_catalog = CatalogItem.objects.all()
    subject = {
        'list_barang': data_catalog,
        'nama': 'Arya Daffa',
        'NPM': '2106650853',
    }  
    return render(request, "katalog.html", subject)
