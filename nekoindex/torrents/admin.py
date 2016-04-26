from django.contrib import admin
from .models import *

for i in (Anime,Torrent, MetaTorrent, MALMeta, Fansub):
    admin.site.register(i)
