from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from torrents.models import Torrent, MALMeta, Anime, Fansub, MetaTorrent

class HomePage(TemplateView):
    template_name="homepage.html"

    def get_context_data(self, **context):
        torrents = Torrent.objects.all()[0:10]
        context.update({
        "last_torrents": torrents,
        'animes': Anime.objects.all().order_by("?")[0:4],
        'animes_emision':  Anime.objects.filter(metatorrent__mal__status__icontains='actualmente').distinct(),
        })
        return context
homepage= HomePage.as_view()


class AnimeDetail(DetailView):
    model = Anime

anime_detail = AnimeDetail.as_view()


class FansubView(TemplateView):
    template_name = "torrents/fansub_list.html"

    def get_context_data(self, **context):
        fansub = Fansub.objects.all()
        context.update({'fansubs': fansub})
        return context

fansub = FansubView.as_view()

class FansubDetail(DetailView):
    model = Fansub
    def get_context_data(self, **context):
        fansub = self.object 
        rilis_group = fansub.release_groups.all()
        metas = MetaTorrent.objects.filter(release_group=rilis_group)
        l = []
        assert False, metas
        for i in metas:
            l.append({'anime_title':i.anime.title,'img':i.mal.image})
        assert False, l
        return context

fansub_detail = FansubDetail.as_view()


