from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from torrents.models import Torrent, MALMeta, Anime

class HomePage(TemplateView):
    template_name="homepage.html"

    def get_context_data(self, **context):
        torrents = Torrent.objects.all()[0:10]
        context.update({
        "last_torrents": torrents,
        'animes': Anime.objects.all().order_by("?")[0:8],
        'animes_emision':  Anime.objects.filter(metatorrent__mal__status__icontains='emisi').distinct().order_by("?")[0:8],
        })
        return context
homepage= HomePage.as_view()


class AnimeDetail(DetailView):
    model = Anime

anime_detail = AnimeDetail.as_view()
