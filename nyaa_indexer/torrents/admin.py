from django.contrib import admin
from .models import *

for i in (Anime, MetaTorrent,  Fansub,Torrent):
    admin.site.register(i)

class AdminMAL(admin.ModelAdmin):
    list_display = ('title','status',"synonyms", "title_en")


admin.site.register(MALMeta, AdminMAL)
#class AdminTorrent(admin.ModelAdmin):
    #list_display = ("full", "url")
    #search_fields = ("full",)
#admin.site.regirrent, AdminTorrent)
