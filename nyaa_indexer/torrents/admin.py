from django.contrib import admin
from .models import *

for i in (Anime, MetaTorrent, MALMeta, Fansub):
    admin.site.register(i)


class AdminTorrent(admin.ModelAdmin):
    list_display = ("full", "url")
    search_fields = ("full",)
admin.site.register(Torrent, AdminTorrent)
