from django.contrib import admin
from .models import *

for i in (Anime, MetaTorrent, MALMeta, Fansub,Torrent):
    admin.site.register(i)


#class AdminTorrent(admin.ModelAdmin):
    #list_display = ("full", "url")
    #search_fields = ("full",)
#admin.site.regirrent, AdminTorrent)
