from django.core.management.base import BaseCommand, CommandError
from nyaa import nyaa
import guessit
from torrents.utils import mal
from torrents.models import Torrent, Anime, MetaTorrent, Fansub, MALMeta

NYAA_USERS = {
'hoshisora.moe':[158741,],
#'puya.se': [239789,],
}

MAL_ANIMES = {
'Hundred':("Hundred", "31338"),
"Seisen Cerberus Ryukoku no Fatalite":("Cerberus",'32595'),
"ReZero kara Hajimeru Isekai Seikatsu":("Re:Zero kara Hajimeru Isekai Seikatsu","31240"),
"Kidou Senshi Gundam UC RE0096":("Mobile Suit Gundam Unicorn RE:0096","32792"),
"Terraformars Revenge": ("Terra formars Revenge","31430"),
"JoJo's Bizarre Adventure Diamond is Unbreakable":("JoJo no Kimyou na Bouken: Diamond wa Kudakenai","31933"),
"Kagewani Shou":("Kagewani: Shou","32682"),
"The World God Only Knows Tenri Arc":("Kami nomi zo Shiru Sekai: Tenri-hen","15117"),
"Kami nomi zo Shiru Sekai: 4-nin to Idol":("Kami nomi zo Shiru Sekai: 4-nin to Idol","10805"),
"Yozakura Quartet Hoshi no Umi": ("Yozakura Quartet: Hoshi no Umi","8457"),
"Wizard Barristers Benmashi Cecil":("Wizard Barristers: Benmashi Cecil","20053"),
}

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for fansub, users in NYAA_USERS.items():
            for user in users:
                offset = 1
                while True:
                    results = nyaa.search(user=user,offset=offset)
                    if not results:
                        break
                    offset +=1
                    for res in results:
                        data = guessit.guessit(res.title)
                        title = data.get("title")
                        kwargs_ = {}
                        if title in MAL_ANIMES:
                            search_title,  mal_id = MAL_ANIMES[title]
                            title = search_title
                            kwargs_ = {'mal_id':mal_id}
                        try:
                            mal_data = mal(title,**kwargs_)
                        except:
                            print ">>>> %s" % title
                            pass
                        torrent,created  = Torrent.objects.get_or_create(full=res.title)
                        torrent.url = res.link
                        torrent.download_url = res.link.replace("view", "download")
                        torrent.save()
                        anime,_ = Anime.objects.get_or_create(title=data.get("title"))
                        fansub,_ = Fansub.objects.get_or_create(name=data.get("release_group"))
                        mal_obj, _ = MALMeta.objects.get_or_create(mal_id=mal_data.id)
                        mal_obj.image = mal_data.img
                        mal_obj.save()
                        meta,_ = MetaTorrent.objects.get_or_create(torrent=torrent,
                                anime=anime, fansub=fansub, mal=mal_obj)
                        meta.episode=data.get("episode", data.get("episode_title"))
                        meta.format=data.get("format", data.get("screen_size"))
                        meta.save()
                        #print "{} {} {} ".format( mal_data.title, mal_data.title_en, title)
