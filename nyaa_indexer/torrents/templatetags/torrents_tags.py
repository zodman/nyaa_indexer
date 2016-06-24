from django import template
from torrents.models import Anime
from django.core.urlresolvers import reverse

register = template.Library()

#@register.simple_tag
#def show_image(anime_name):
    #anime = Anime.objects.get(title=anime_name)
    #return anime.meta.mal.image

@register.simple_tag
def show_anime(anime_name):
    anime = Anime.objects.get(title=anime_name)
    return anime
