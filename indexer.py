from nyaa import nyaa
import guessit
from utils import mal

NYAA_USERS = {
'hoshisora.moe':[158741,],
'puya.se': [239789,],
}

def main():

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
                    title = data["title"]
                    release_group = data["release_group"]
                    mal_data = mal(title)
                    print mal_data.id, mal_data.title, mal_data.title_en, title

if __name__=="__main__":
    main()
