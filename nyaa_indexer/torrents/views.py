from django.shortcuts import render
from django.views.generic import TemplateView
from torrents.models import Torrent, MALMeta

class HomePage(TemplateView):
    template_name="homepage.html"

    def get_context_data(self, **context):
        torrents = Torrent.objects.all()
        context.update({"last_torrents": torrents})
        return context
homepage= HomePage.as_view()
