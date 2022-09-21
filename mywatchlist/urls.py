# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import watchlist
from mywatchlist.views import xml_funct
from mywatchlist.views import json_funct
from mywatchlist.views import id_funct_json
from mywatchlist.views import id_funct_xml

app_name = 'watchlist'

urlpatterns = [
    path('', watchlist, name = 'watchlist'),
    path('xml/', xml_funct, name='xml_funct'),
    path('json/', json_funct, name='json_funct'),
    path('xml/<int:id>', id_funct_xml, name='id_funct_xml'),
    path('json/<int:id>', id_funct_json, name='id_funct_json'),
]