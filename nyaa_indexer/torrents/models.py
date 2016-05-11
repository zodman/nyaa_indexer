from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
import guessit


class Fansub(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class Anime(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    class Meta:
        ordering =("-created_at",'-id',)

    @property
    def meta(self):
        meta = self.metatorrent_set.first()
        return meta

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Anime,self).save(*args,**kwargs)

    def __unicode__(self):
        return u"%s" % self.title

class MALMeta(models.Model):
    mal_id = models.PositiveIntegerField(unique=True, null = False, blank = False)
    synopsys = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    title_en = models.CharField(max_length=100, null=True, blank=True)
    resumen = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    synonyms = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    alternative_title = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" %self.mal_id


class MetaTorrent(models.Model):
    fansub = models.ForeignKey("Fansub")
    anime = models.ForeignKey("Anime")
    mal = models.ForeignKey("MALMeta")
    torrent = models.OneToOneField("Torrent")
    episode = models.CharField(max_length=20, null=True, blank=True)
    format = models.CharField(max_length=10,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % (self.id, )


class Torrent(models.Model):
    full = models.TextField(unique=True)
    url = models.URLField()
    download_url = models.URLField()
    download_magnet = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =("-created_at",'-id',)

    def __unicode__(self):
        return u"%s" % self.full
		
    @property	
	def guessit(self):
		data = guessit.guessit(self.full)
		return data

