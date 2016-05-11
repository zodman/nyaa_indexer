from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import make_aware
from nyaa import nyaa
import guessit
from torrents.utils import mal
from torrents.models import Torrent, Anime, MetaTorrent, Fansub, MALMeta
from torrents.mal_animes import MAL_ANIMES, BYPASS
from tqdm import tqdm

NYAA_USERS = {
'hoshisora.moe':[158741,],
'puya.se': [239789,],
'mabushii':[81074,]
}


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        results = []
        for fansub, users in tqdm(NYAA_USERS.items()):
            for user in users:
                offset = 1
                while True:
                    results_ = nyaa.search(user=user,offset=offset)
                    if not results_:
                        break
                    offset +=1
                    results+=results_

        for res in tqdm(results):
            flag_next = False
            for j in BYPASS:
                if j.lower() in res.title.lower():
                    flag_next = True
                    break
            if flag_next: continue
            tqdm.write("%s %s" % (res.title, make_aware(res.date)))
            torrent,created  = Torrent.objects.get_or_create(full=res.title, 
                url=res.link, download_url = res.link.replace("view","download"),
                date=make_aware(res.date)
                )
            full = res.title.replace("[BATCH]","").replace("[Batch]","")
            data = guessit.guessit(full, {"episode_prefer_number":True})
            title = data.get("title")
            kwargs_ = {}
            if title in MAL_ANIMES:
                search_title,  mal_id = MAL_ANIMES[title]
                title = search_title
                kwargs_ = {'mal_id':mal_id}
            mal_data = mal(title,**kwargs_)
            anime,_ = Anime.objects.get_or_create(title=data.get("title"))
            fansub,_ = Fansub.objects.get_or_create(name=data.get("release_group"))
            mal_obj, _ = MALMeta.objects.get_or_create(mal_id=mal_data.id)
            mal_obj.title = mal_data.title
            mal_obj.image = mal_data.img
            mal_obj.synopsys = mal_data.synopsys
            mal_obj.resumen = mal_data.resumen
            mal_obj.synonyms = mal_data.synonyms
            mal_obj.title_en = mal_data.title_en
            mal_obj.status = mal_data.status
            mal_obj.save()
            meta,_ = MetaTorrent.objects.get_or_create(
                    anime=anime, torrent=torrent,fansub=fansub, mal=mal_obj)
            meta.episode=data.get("episode", data.get("episode_title"))
            meta.format=data.get("format", data.get("screen_size"))
            meta.save()


