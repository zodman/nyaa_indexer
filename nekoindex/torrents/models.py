from __future__ import unicode_literals
from django.db import models



class Fansub(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __unicode__(self):
        return self.name


class Anime(models.Model):
    title = models.CharField(max_length=300, unique=True)

    def __unicode__(self):
        return self.title

class MALMeta(models.Model):
    mal_id = models.PositiveIntegerField(unique=True)
    synoms = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    alternative_title = models.CharField(max_length=300, null=True, blank=True)
    def __unicode__(self):
        return self.mal_id


class MetaTorrent(models.Model):
    torrent = models.ForeignKey("Torrent")
    fansub = models.ForeignKey("Fansub")
    anime = models.ForeignKey("Anime")
    mal = models.ForeignKey("MALMeta")
    episode = models.CharField(max_length=20, null=True)
    format = models.CharField(max_length=10,null=True)

    def __unicode__(self):
        return u"%s" % self.id


class Torrent(models.Model):
    full = models.TextField(unique=True)
    url = models.URLField()
    download_url = models.URLField()
    download_magnet = models.TextField(null=True)

    def __unicode__(self):
        return self.full

