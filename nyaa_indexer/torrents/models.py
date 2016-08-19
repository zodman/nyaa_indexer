from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
import guessit
from django.core.cache import cache 


class ReleaseGroup(models.Model):
    name = models.CharField(max_length=100,unique=True)
    alias = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name


class Fansub(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    release_groups = models.ManyToManyField('ReleaseGroup')

    def __unicode__(self):
        return u"%s" % self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Fansub,self).save(*args,**kwargs)

class Anime(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
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
    release_group = models.ForeignKey("ReleaseGroup")
    anime = models.ForeignKey("Anime")
    mal = models.ForeignKey("MALMeta")
    torrent = models.OneToOneField("Torrent",  on_delete=models.CASCADE)
    episode = models.CharField(max_length=20, null=True, blank=True)
    format = models.CharField(max_length=10,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % (self.id, )


class Torrent(models.Model):
    full = models.TextField()
    url = models.URLField()
    download_url = models.URLField()
    download_magnet = models.TextField(null=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =("-created_at",'-id',)
        unique_together = ("full","url")

    def __unicode__(self):
        return u"%s" % self.full
		
    @property	
    def guessit(self):
	full_data = cache.get(slugify(self.full))
	if full_data is None:
            data = guessit.guessit(self.full)
            cache.set(slugify(self.full), data)
            full_data = data
        return full_data

