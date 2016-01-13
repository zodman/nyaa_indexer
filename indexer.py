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
                    #issue https://github.com/guessit-io/guessit/issues/245
                    try:
                        title = data["title"]
                    except KeyError:
                        title = data.get("film_title")
                    release_group = data["release_group"]
                    print mal(title)
                        



if __name__=="__main__":
    main()
