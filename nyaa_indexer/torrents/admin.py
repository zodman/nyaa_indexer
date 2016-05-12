from django.contrib import admin
from .models import *

admin.site.register(Anime)

class AdminRilis(admin.ModelAdmin):
    list_display = ("name", "get_torrents")

    def get_torrents(self,obj):
        a = obj.metatorrent_set.all()
        if a.count() >10 :
            return "1"
        else:
            return "%s" % [ "%s\n" %i.torrent.full for i in a]
admin.site.register(ReleaseGroup, AdminRilis)


class AdminMAL(admin.ModelAdmin):
    list_display = ('title','status',"synonyms", "title_en")
admin.site.register(MALMeta, AdminMAL)

class AdminTorrent(admin.ModelAdmin):
    list_display = ("full", "url")
    search_fields = ("full",)
admin.site.register(Torrent, AdminTorrent)


class AdminFansub(admin.ModelAdmin):
    filter_horizontal  = ("release_groups",)
admin.site.register(Fansub, AdminFansub)


class AdminMeta(admin.ModelAdmin):
    list_display = ("pk", "full","release_group","anime")
    search_fields = ("torrent__full", "release_group__name", "anime__title",)
    def full(self, obj):
        return obj.torrent.full

admin.site.register(MetaTorrent, AdminMeta)
